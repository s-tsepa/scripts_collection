#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/resource.h>


int main() {
    int iter_count = 10;

    struct rusage start, end;

    // Measure time usage of program at start
    getrusage(RUSAGE_SELF, &start);
    for(int i = 0; i < iter_count; i++) {
        sleep(1);
        int n_bytes = 1000 * 1024 * 1024;
        // Allocate 1GB of memory
        int* ptr1 = malloc(n_bytes);
        // Fill them with zeros
        memset(ptr1, 0, n_bytes);
    }
    // Measure time usage at the end
    getrusage(RUSAGE_SELF, &end);

    // Subtract measurements end - start, to get usage of program during loop execution
    float diff_user = (end.ru_utime.tv_sec - start.ru_utime.tv_sec) + 1e-6 * (end.ru_utime.tv_usec - start.ru_utime.tv_usec);
    float diff_system = (end.ru_stime.tv_sec - start.ru_stime.tv_sec) + 1e-6*(end.ru_stime.tv_usec - start.ru_stime.tv_usec);
    printf("CPU time: %.01f sec user, %.01f sec system\n", diff_user, diff_system);
}
