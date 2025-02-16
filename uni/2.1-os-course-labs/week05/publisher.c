#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>

#define FILENAME "/tmp/ex1"
#define MAX_LEN 1024

int main(int argc, char* argv[]) {
    int cnt;
    sscanf(argv[1], "%d", &cnt);
    printf("%d\n", cnt);


    mkfifo(FILENAME, 0666);
    int fd, n;
    char input[MAX_LEN];

    while (1) {
        fd = open(FILENAME, O_WRONLY);
        fgets(input, MAX_LEN, stdin);
        n = strlen(input);
        if (n < 1) { return EXIT_SUCCESS; }

        for (int i = 0; i < cnt; ++i) {
            sleep(1);
            write(fd, input, MAX_LEN);
        }

        close(fd);
    }
}