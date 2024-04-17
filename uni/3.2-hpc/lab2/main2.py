import multiprocessing
import time

import numba
import numpy as np
import matplotlib.pyplot as plt
from numba import jit, cuda

L = 1.0  # Length of the domain
T = 2.0  # Final time
N = 1000  # Number of time steps
M = 200  # Number of spatial steps
dx = L / M
dt = T / N


thread_cnt_param = [1, 2, 4, 8]
N_param = list(range(1000, 11000, 1000))
dt_values = []

x = np.linspace(0, L, M + 1)


def solve_wave_equation_part(u, x_prime, start, end):
    for n in range(start, end):
        for m in range(1, M):
            u[n + 1, m] = u[n, m] + dt * x_prime[m] + \
                          (dt ** 2 / 2) * (np.exp(np.cos(x[m])) / 10) * \
                          ((u[n, m + 1] - 2 * u[n, m] + u[n, m - 1]) / dx ** 2)
        for m in range(1, M):
            x_prime[m] = (u[n + 1, m + 1] - u[n + 1, m - 1]) / (2 * dx)


def run_sample_plot_animation():
    u = np.zeros((N + 1, M + 1))
    u[0] = 0.1 * np.sin(np.pi * x)

    u[:, 0] = 0
    u[:, -1] = 0

    x_prime = np.zeros_like(x)

    solve_wave_equation_part(u, x_prime, 0, N)

    # fig, ax = plt.subplots()
    # ax.set_xlim(0, 1)
    # ax.set_ylim(-0.2, 0.2)
    # line, = ax.plot([], [], lw=2)
    #
    # def init():
    #     line.set_data([], [])
    #     return line,
    #
    # def animate(i):
    #     line.set_data(x, u[i])
    #     return line,
    #
    # ani = FuncAnimation(fig, animate, frames=N + 1, init_func=init, blit=True)
    # ani.save("TLI.gif", dpi=300, writer=PillowWriter(fps=25))

    plt.figure(figsize=(8, 6))

    for n in range(0, N + 1, 50):
        plt.plot(x, u[n], label=f"t={n * dt:.2f}")

    plt.xlabel('x')
    plt.ylabel('u')
    plt.title('Wave animation')
    plt.legend()
    plt.grid(True)
    plt.show()


def run_cpu_perf_analysis_chart():

    # Function to perform performance analysis
    def performance_analysis(num_threads_list, N_values):
        results = {}
        for N in N_values:
            times = []
            for num_threads in num_threads_list:
                u = np.zeros((N + 1, M + 1))
                x_prime = np.zeros_like(x)

                # Split the work among threads
                chunk_size = N // num_threads
                processes = []
                start_time = time.time()
                for i in range(num_threads):
                    start = i * chunk_size
                    end = (i + 1) * chunk_size if i < num_threads - 1 else N
                    process = multiprocessing.Process(target=solve_wave_equation_part, args=(u, x_prime, start, end))
                    processes.append(process)
                    process.start()
                for process in processes:
                    process.join()
                end_time = time.time()
                times.append(end_time - start_time)
            results[N] = times
        return results

    # Create dt values for each N
    for N in N_param:
        dt_values.append(T / N)

    # Measure performance
    results = performance_analysis(thread_cnt_param, N_param)

    # Plot performance analysis
    for N in N_param:
        plt.plot(thread_cnt_param, results[N], label=f"N={N}, dt={dt_values[N // 1000 - 1]:.4f}")

    plt.xlabel('Number of Threads')
    plt.ylabel('Time (seconds)')
    plt.title('Performance Analysis for CPU Parallelization')
    plt.legend()
    plt.grid(True)
    plt.show()


def run_gpu_perf_analysis_table():
    # Define the wave equation solver on GPU (naive approach)
    @cuda.jit
    def solve_wave_equation_gpu_naive(u, x_prime):
        n, m = cuda.grid(2)
        if 0 < n < N and 0 < m < M:
            u[n + 1, m] = u[n, m] + dt * x_prime[n, m] + \
                          (dt ** 2 / 2) * (np.exp(np.cos(x[m])) / 10) * \
                          ((u[n, m + 1] - 2 * u[n, m] + u[n, m - 1]) / dx ** 2)
            if m > 0 and m < M - 1:
                x_prime[n, m] = (u[n + 1, m + 1] - u[n + 1, m - 1]) / (2 * dx)

    # Define the wave equation solver on GPU (optimized with shared memory and barriers)
    @cuda.jit
    def solve_wave_equation_gpu_optimized(u, x_prime):
        n, m = cuda.grid(2)
        if 0 < n < N and 0 < m < M:
            local_u = cuda.shared.array((16, 16), dtype=numba.float32)
            local_x_prime = cuda.shared.array((16, 16), dtype=numba.float32)

            local_u[n % 16, m % 16] = u[n, m]
            local_x_prime[n % 16, m % 16] = x_prime[n, m]

            cuda.syncthreads()

            u[n + 1, m] = local_u[n % 16, m % 16] + dt * local_x_prime[n % 16, m % 16] + \
                          (dt ** 2 / 2) * (np.exp(np.cos(x[m])) / 10) * \
                          ((local_u[(n + 1) % 16, m % 16] - 2 * local_u[n % 16, m % 16] + local_u[
                              (n - 1) % 16, m % 16]) / dx ** 2)

            if m > 0 and m < M - 1:
                x_prime[n, m] = (local_u[n % 16, (m + 1) % 16] - local_u[n % 16, (m - 1) % 16]) / (2 * dx)

    # Function to solve the wave equation using CPU
    def solve_wave_equation_cpu(u, x_prime):
        for n in range(N):
            for m in range(1, M):
                u[n + 1, m] = u[n, m] + dt * x_prime[n, m] + \
                              (dt ** 2 / 2) * (np.exp(np.cos(x[m])) / 10) * \
                              ((u[n, m + 1] - 2 * u[n, m] + u[n, m - 1]) / dx ** 2)
            for m in range(1, M):
                x_prime[n + 1, m] = (u[n + 1, m + 1] - u[n + 1, m - 1]) / (2 * dx)

    u_cpu = np.zeros((N + 1, M + 1))
    u_gpu_naive = cuda.to_device(np.zeros((N + 1, M + 1), dtype=np.float32))
    u_gpu_optimized = cuda.to_device(np.zeros((N + 1, M + 1), dtype=np.float32))
    x_prime_cpu = np.zeros((N + 1, M + 1))
    x_prime_gpu = cuda.to_device(np.zeros((N + 1, M + 1), dtype=np.float32))

    threadsperblock = (16, 16)
    blockspergrid_x = (N + threadsperblock[0] - 1) // threadsperblock[0]
    blockspergrid_y = (M + threadsperblock[1] - 1) // threadsperblock[1]
    blockspergrid = (blockspergrid_x, blockspergrid_y)

    # Solve the wave equation using CPU
    start_time = time.time()
    solve_wave_equation_cpu(u_cpu, x_prime_cpu)
    cpu_time = time.time() - start_time

    # Solve the wave equation using GPU (naive approach)
    start_time = time.time()
    solve_wave_equation_gpu_naive[blockspergrid, threadsperblock](u_gpu_naive, x_prime_gpu)
    cuda.synchronize()
    gpu_naive_time = time.time() - start_time

    # Solve the wave equation using GPU (optimized approach)
    start_time = time.time()
    solve_wave_equation_gpu_optimized[blockspergrid, threadsperblock](u_gpu_optimized, x_prime_gpu)
    cuda.synchronize()
    gpu_optimized_time = time.time() - start_time

    u_gpu_naive.copy_to_host()
    u_gpu_optimized.copy_to_host()

    # Print performance table
    print("Performance Table:")
    print(f"{'':20}{'CPU':^30}{'GPU (Naive)':^30}{'GPU (Optimized)':^30}")
    print(
        f"{'Execution Time (s)':<20}{cpu_time:^30.6f}{gpu_naive_time:^30.6f}{gpu_optimized_time:^30.6f}")


if __name__ == "__main__":
    run_sample_plot_animation()
    # run_cpu_perf_analysis_chart()
    # run_gpu_perf_analysis_table()