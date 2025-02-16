#include <stdio.h>
#include <stdlib.h>

void sort(int ** arr, int rows) {
    for (int i = 0; i < rows; i++) {
        for (int j = i +1; j < rows; ++j) {
            if (arr[i][0] > arr[j][0] || (arr[i][0] == arr[j][0] && arr[i][1] > arr[j][1])) {
                int *swap = arr[i];
                arr[i] = arr[j];
                arr[j] = swap;
            }
        }
    }
}

void print_2d_ints_arr(int **arr, int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int n;
    scanf("%d", &n);

    int **arr;
    arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        arr[i] = malloc(2 * sizeof(int));
    }
    int l = 0;

    for (int i = 0; i < n; ++i) {
        int at, bt;
        scanf("%d%d", &at, &bt);
        arr[i][0] = at;
        arr[i][1] = bt;
    }

    print_2d_ints_arr(arr, n, 2);
    printf("\n");

//    qsort (arr, sizeof(arr)/sizeof(*arr), sizeof(*arr), comp);
    sort(arr, n);

    print_2d_ints_arr(arr, n, 2);


    int cur_tick = 0;
    int sum_compl_time = 0;
    int sum_tat_time = 0;

    for (int i = 0; i < n; ++i) {
        int at = arr[i][0];
        int bt = arr[i][1];

        if (cur_tick < at) {
            cur_tick = at;
        }

        int waiting_time = cur_tick - at;
        printf("(%d, %d) proc\n", at, bt);
        printf("WT: %d\n", waiting_time);

        cur_tick += bt;

        printf("CT: %d\n", cur_tick);

        sum_compl_time += cur_tick;

        printf("TAT: %d\n", bt);

        sum_tat_time += bt;
        printf("\n");
    }

    float avg_compl_time = (float) sum_compl_time / (float) n;
    float avg_tat_time = (float) sum_tat_time / ( float) n;

    printf("Avg CT, TAT: %f, %f", avg_compl_time, avg_tat_time);
}
