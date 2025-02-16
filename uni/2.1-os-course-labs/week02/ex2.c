#include<limits.h>
#include <float.h>
#include<stdio.h>
#include <string.h>

void recursive(char* ch) {
    if (*(ch + 1) == '\0' || *(ch + 1) == '.') {
        printf("%c", *ch);
    } else {
        recursive(ch + 1);
        printf("%c", *ch);
    }
}

int main() {
    char arrs[256];
    gets(arrs);

//    printf("%p\n", &arrs[0]);
//    printf("%c\n", *(&arrs[0]+1));
//    printf("%p\n", &arrs[0]+1);

    recursive(&arrs[0]);

    return 0;
}
