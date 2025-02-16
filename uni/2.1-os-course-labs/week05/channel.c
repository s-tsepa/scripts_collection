#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define MAX_LEN 256


int main() {
     int fd[2];

     if (pipe(fd) == -1) {
         return EXIT_FAILURE;
     }

     int pid = fork();
     if (pid < 0) {
         return EXIT_FAILURE;
     }

     if (pid == 0) {
         char input[MAX_LEN];
         scanf("%s", input);

         int n = strlen(input);
         write(fd[1], &n, sizeof(int));
         write(fd[1], input, strlen(input));
     } else {
         close(fd[1]);
         char str[MAX_LEN];

         int n; read(fd[0], &n, sizeof(int));

         read(fd[0], str, sizeof(char) * n);

         printf("Your message: %s", str);
     }
}
