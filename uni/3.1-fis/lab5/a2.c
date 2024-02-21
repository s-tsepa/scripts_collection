#include <stdio.h>
#include <string.h>

int main(void) {
    char buff[15];
    int pass = 0;
    char* pwd = "password";

    printf("\n Enter password : \n");
    if (fgets(buff, sizeof(buff), stdin) != NULL) {
        if (strcmp(buff, pwd) == 0) {
            printf("\n Correct Password \n");
            pass = 1;
        } else {
            printf("\n Wrong Password \n");
        }
    } else {
        printf("\n Input error \n");
    }

    if (pass) {
        printf("\n User has successfully logged in \n");
    }

    return 0;
}
