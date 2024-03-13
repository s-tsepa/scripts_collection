
#include <vector>
#include <CL/opencl.hpp>
#include <iostream>
#include <fstream>

#include <chrono>
#include <iomanip>


class Math {

public:
	static float dotProductSerial(const std::vector<float> &a, const std::vector<float> &b) {
		float result = 0.0f;
		for (size_t i = 0; i < a.size(); ++i) {
			result += a[i] * b[i];
		}
		return result;
	}

	static float dotProductOpenMP(const std::vector<float> &a, const std::vector<float> &b) {
		float result = 0.0f;
	#pragma omp parallel for reduction(+ : result)
		for (size_t i = 0; i < a.size(); ++i) {
			result += a[i] * b[i];
		}
		return result;
	}

	static float dotProductOpenCLNaive(const std::vector<float> &vec1, const std::vector<float> &vec2) {
		// Get available platforms
		std::vector<cl::Platform> platforms;
		cl::Platform::get(&platforms);

		if (platforms.empty()) {
			std::cerr << "No OpenCL platforms found." << std::endl;
			return 0.0f;
		}

		std::vector<cl::Device> devices;
		platforms[0].getDevices(CL_DEVICE_TYPE_GPU, &devices);

		if (devices.empty()) {
			std::cerr << "No GPU devices found." << std::endl;
			return 0.0f;
		}

		cl::Context context(devices);
		cl::CommandQueue queue(context, devices[0]);

		std::string kernelSource
			= "__kernel void dot_product(__global const float* vec1, __global const float* vec2, "
			  "__global float* result, const unsigned int n) {\n"
			  "    int gid = get_global_id(0);\n"
			  "    if (gid < n) {\n"
			  "        result[gid] = vec1[gid] * vec2[gid];\n"
			  "    }\n"
			  "}\n";

		cl::Program::Sources sources;
		sources.push_back({kernelSource.c_str(), kernelSource.length()});

		cl::Program program(context, sources);

		cl::Kernel kernel(program, "dot_product");

		cl::Buffer bufferVec1(context,
							  CL_MEM_READ_ONLY | CL_MEM_COPY_HOST_PTR,
							  sizeof(float) * vec1.size(),
							  const_cast<float *>(vec1.data()));
		cl::Buffer bufferVec2(context,
							  CL_MEM_READ_ONLY | CL_MEM_COPY_HOST_PTR,
							  sizeof(float) * vec2.size(),
							  const_cast<float *>(vec2.data()));
		cl::Buffer bufferResult(context, CL_MEM_WRITE_ONLY, sizeof(float) * vec1.size());

		kernel.setArg(0, bufferVec1);
		kernel.setArg(1, bufferVec2);
		kernel.setArg(2, bufferResult);
		kernel.setArg(3, static_cast<unsigned int>(vec1.size()));

		queue.enqueueNDRangeKernel(kernel, cl::NullRange, cl::NDRange(vec1.size()));

		std::vector<float> result(vec1.size());
		queue.enqueueReadBuffer(bufferResult, CL_TRUE, 0, sizeof(float) * vec1.size(), result.data());

		float dotProduct = 0.0f;
		for (float val : result) {
			dotProduct += val;
		}

		return dotProduct;
	}

//	static float dotProductOpenCLOptimized(const std::vector<float> &a, const std::vector<float> &b);

};

void printCPUInfo() {
    std::ifstream cpuinfo("/proc/cpuinfo");
    std::string line;
    while (std::getline(cpuinfo, line)) {
        if (line.substr(0, 6) == "model:" || line.substr(0, 7) == "cpu MHz" || line.substr(0, 9) == "cpu cores" || line.substr(0, 8) == "MemTotal") {
            std::cout << line << std::endl;
        }
    }
    cpuinfo.close();
}

void printGPUInfo() {
    cl_platform_id platform;
    cl_device_id device;
    cl_uint numPlatforms;
    cl_uint numDevices;

    clGetPlatformIDs(0, nullptr, &numPlatforms);
	clGetPlatformIDs(1, &platform, nullptr);
    clGetDeviceIDs(platform, CL_DEVICE_TYPE_GPU, 0, nullptr, &numDevices);
    clGetDeviceIDs(platform, CL_DEVICE_TYPE_GPU, 1, &device, nullptr);

    char buffer[1024];
    clGetDeviceInfo(device, CL_DEVICE_NAME, sizeof(buffer), buffer, nullptr);
    std::cout << "GPU Model: " << buffer << std::endl;

    clGetDeviceInfo(device, CL_DEVICE_MAX_CLOCK_FREQUENCY, sizeof(buffer), buffer, nullptr);
    std::cout << "Clock Frequency: " << buffer << " MHz" << std::endl;

    clGetDeviceInfo(device, CL_DEVICE_MAX_COMPUTE_UNITS, sizeof(buffer), buffer, nullptr);
    std::cout << "Number of Shader Cores: " << buffer << std::endl;

    cl_ulong memSize;
    clGetDeviceInfo(device, CL_DEVICE_GLOBAL_MEM_SIZE, sizeof(memSize), &memSize, nullptr);
    std::cout << "GRAM Size: " << memSize / (1024 * 1024) << " MB" << std::endl << std::endl;
}

int main()
{
    std::cout << "Name: Stepan" << std::endl;
    std::cout << "Surname: Tsepa" << std::endl;
    std::cout << "Programming assignment #01" << std::endl;

    std::cout << "\nCPU Information:" << std::endl;
    printCPUInfo();

    std::cout << "\nGPU Information:" << std::endl;
    printGPUInfo();

    // --- Calculation ---

    const std::vector<size_t> arraySizes = {1000, 10000, 100000, 1000000};

    std::cout << std::setw(10) << "Array Size" << std::setw(15) << "Serial Time" << std::setw(15)
              << "OMP Time" << std::setw(15) << "OMP Speedup" << std::setw(15) << "OpenCL 1 Time"
              << std::setw(20) << "OpenCL 1 Speedup" << std::setw(15) << "OpenCL 2 Time"
              << std::setw(20) << "OpenCL 2 Speedup" << std::endl;

    for (size_t size : arraySizes) {
        std::vector<float> vec1(size, 1.0f);
        std::vector<float> vec2(size, 0.5f);

        auto start = std::chrono::steady_clock::now();
        float serialResult = Math::dotProductSerial(vec1, vec2);
        auto end = std::chrono::steady_clock::now();
        std::chrono::duration<double> serialTime = end - start;

        start = std::chrono::steady_clock::now();
        float parallelResult = Math::dotProductOpenMP(vec1, vec2);
        end = std::chrono::steady_clock::now();
        std::chrono::duration<double> parallelTime = end - start;

        start = std::chrono::steady_clock::now();
        float naiveOpenCLResult = Math::dotProductOpenCLNaive(vec1, vec2);
        end = std::chrono::steady_clock::now();
        std::chrono::duration<double> naiveOpenCLTime = end - start;

        double ompParallelSpeedup = serialTime.count() / parallelTime.count();
        double naiveOpenCLSpeedup = serialTime.count() / naiveOpenCLTime.count();

        std::cout << std::setw(10) << size << std::fixed << std::setprecision(6) << std::setw(15)
                  << serialTime.count() << std::setw(15) << parallelTime.count() << std::setw(15)
                  << ompParallelSpeedup << std::setw(15) << naiveOpenCLTime.count() << std::setw(20)
                  << naiveOpenCLSpeedup << std::setw(15) << std::endl;

		float threshold = 0.0001f;
        bool parallelCorrect = std::abs(serialResult - parallelResult) < threshold;
		bool openCLCorrect = std::abs(serialResult - naiveOpenCLResult) < threshold;

    	if (parallelCorrect && openCLCorrect) {
    		std::cout << "All results are equal" << std::endl;
    	}

		std::cout << serialResult << ", " << parallelResult << ", " << naiveOpenCLResult << std::endl;
    }

    return 0;
}
