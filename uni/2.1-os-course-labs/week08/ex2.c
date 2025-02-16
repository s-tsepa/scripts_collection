#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int main() {
    int iter_count = 10;


    for(int i = 0; i < iter_count; i++) {
        sleep(1);
        int n_bytes = 1000 * 1024 * 1024;
        // Allocate 1GB of memory
        int* ptr1 = malloc(n_bytes);
        // Fill them with zeros
        memset(ptr1, 0, n_bytes);
    }
}
