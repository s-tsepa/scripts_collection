#include <stdio.h>
#include <string.h>

int main(void)
{
    char buff[15];
    int pass = 0;

    printf("\n Enter password : \n");
    gets(buff);

    if(strcmp(buff, "password"))
    {
        printf ("\n Wrong Password \n");
    }
    else
    {
        printf ("\n Correct Password \n");
        pass = 1;
    }

    if(pass)
    {
       /* Grant login access to user*/
        printf ("\n User has successfully logged in \n");
    }

    return 0;
}
