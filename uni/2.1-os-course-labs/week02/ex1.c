#include<limits.h>
#include <float.h>
#include <stdio.h>

int main() {
    int i;
    unsigned short int usi;
    long int sli;
    float f;
    double d;

    i = INT_MAX;
    usi = USHRT_MAX;
    sli = LONG_MAX;
    f = FLT_MAX;
    d = DBL_MAX;

    printf("%lu %d\n", sizeof(i), i);
    printf("%lu %u\n", sizeof(usi), usi);
    printf("%lu %ld\n", sizeof(sli), sli);
    printf("%lu %f\n", sizeof(f), f);
    printf("%lu %f\n", sizeof(d), d);

    return 0;
}
