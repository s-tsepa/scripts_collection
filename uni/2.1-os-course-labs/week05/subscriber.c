#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <time.h>

#define FILENAME "/tmp/ex1"
#define MAX_LEN 1024

int main() {
    mkfifo(FILENAME, 0666);
    int fd;
    char msg[MAX_LEN];

    srand ( time(NULL) );
    int microsec_to_sleep = 1000000 + (rand() % 3000000);
    printf("Rand: %d\n", microsec_to_sleep);


    while (1) {
        fd = open(FILENAME, O_RDONLY);
        if (read(fd, msg, MAX_LEN) > 0) {
            printf("Subscriber received msg: %s", msg);
        }
        close(fd);
        usleep(microsec_to_sleep);
    }
}