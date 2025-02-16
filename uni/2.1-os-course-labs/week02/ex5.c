#include<stdio.h>
#include<stdlib.h>
#include <string.h>
#include <ctype.h>

int max(int a, int b) {
    if (a > b) { return a; }
    else { return b; }
}

int tribonacci(int n) {
    int t1 = 0, t2 = 1, t3 = 1, t4 = 2;

    if (n == 0) { return 0; }
    if (n == 1) { return 1; }
    if (n == 2) { return 1; }
    if (n == 3) { return 2; }

    for (int i = 0; i < n - 3; ++i) {
        if (i % 4 == 0) {
            t1 = t2 + t3 + t4;
        } else if (i % 4 == 1) {
            t2 = t1 + t3 + t4;
        } else if (i % 4 == 2) {
            t3 = t1 + t2 + t4;
        } else if (i % 4 == 3) {
            t4 = t1 + t2 + t3;
        }
    }

    return max(max(t1, t2), max(t3, t4));
}

int main() {
    int res4 = tribonacci(4);
    int res36 = tribonacci(36);

    printf("%d\n", res4);
    printf("%d\n", res36);

    return 0;
}
