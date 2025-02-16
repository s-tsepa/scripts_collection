#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int foo(int age) {
	int result;
	
	result = 2022 - age;
	
	return result;
}

int main() {

    const n = 5;

    const int x = 10;
    const int *q = &x;

    const int *const p = (const int*) malloc(sizeof(const int) * 5);

    int* pp = (int*) p;
    for (int i = 0; i < n; ++i) {
        pp[i] = x;
        printf("%p\n", p+i);
    }

    for (int i = 0; i < n; ++i) {
        int c;
        scanf("%d", &c);
        pp[i] = c;
    }

    for (int i = 0; i < n; ++i) {
        int xx = p[i];
        pp[i] = foo(xx);
    }

    free(pp);


	return EXIT_SUCCESS;
}
