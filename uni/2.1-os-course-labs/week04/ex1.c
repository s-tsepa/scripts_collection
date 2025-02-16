#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>


// <WRITE YOUR CODE HERE>



int main(void){

    clock_t time = clock();
    printf("IDs: %d %d\n", getpid(), getppid());
    printf("Time: %f\n\n", (double) (clock() - time)*1000.0f/CLOCKS_PER_SEC);

    for (int i = 0; i < 2; ++i) {
        if (fork() == 0) {
            time = clock();
            printf("IDs: %d %d\n", getpid(), getppid());
            printf("Time: %f\n\n", (double) (clock() - time)*1000.0f/CLOCKS_PER_SEC);
            exit(EXIT_SUCCESS);
        }
    }

    for (int i = 0; i < 2; ++i) {
        wait(NULL);
    }

	return EXIT_SUCCESS;

}
