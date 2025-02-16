#include <stdlib.h>
#include <stdio.h>
#include <time.h>


int main() {
    srand(time(NULL));

    int size_start; scanf("%d",&size_start);
    int* arr1 = malloc(sizeof(int) * size_start);

    for(int i = 0; i < size_start; i++) {
        arr1[i] = 100;
    }

    for(int i = 0; i < size_start; i++) {
        printf("%d ", arr1[i]);
    } printf("\n");

    int size_end; scanf("%d", &size_end);
    arr1 = realloc(arr1, sizeof(int) * size_end);

    for(int i = 0; i < size_end; i++) {
        printf("%d ", *(arr1 + i));
    } printf("\n");
}
