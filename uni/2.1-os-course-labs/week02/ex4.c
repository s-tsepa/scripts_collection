#include<stdio.h>
#include <string.h>
#include <ctype.h>

int count(char* s, char c) {
    int count = 0;

    for (int i = 0; i < strlen(s); ++i) {
        if (tolower(s[i]) == c) { count++; }
    }
    return count;
}

void countAll(char* s) {
    for (int i = 0; i < strlen(s); ++i) {
        char c = tolower(s[i]);
        int count_s = count(s, c);
        printf("%c: %d, ", c, count_s);
    }
}

int main() {

    char s[256]; gets(s);

    countAll(s);

    return 0;
}
