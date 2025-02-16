#include<stdio.h>
#include<stdlib.h>

long long int convert(long long int n, int s, int t) {
    if (s > 10 || s < 2 || t > 10 || t < 2) { printf("cannot convert!"); exit(0); }

    int cum = 0;
    int fac = 1;
    while (n > 1) {
        int nn = n % 10;

        if (nn > s) { printf("cannot convert!"); exit(0); }

        n /= 10;
        cum += nn * fac;
        fac *= s;
    }

    cum += n * fac;

    int cur_power = 1;
    while (cur_power < cum) {
        cur_power *= t;
    } cur_power /= t;

    char res[256];

    int i = 0;

    while (cur_power >= 1) {
        int razryad = cum / cur_power;

        cum -= razryad * cur_power;

        res[i] = (char) (razryad + '0');

        i++;
        cur_power /= t;
    }

    res[i] = '\0';

    long long int resn;
    sscanf(res, "%ld", &resn);

    return resn;
}

int main() {
    long long int n; int s, t;

    printf("Enter n: ");
    scanf("%ld", &n);

    printf("Enter s: ");
    scanf("%d", &s);

    printf("Enter t: ");
    scanf("%d", &t);

    long long int res;
    res = convert(n, s, t);

    printf("%ld", res);

    return 0;
}
