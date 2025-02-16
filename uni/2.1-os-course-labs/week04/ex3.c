#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main(int argc, char* argv[]){
    int n;
    for (int i = 0; i < argc; ++i) {
        sscanf(argv[i], "%d", &n);
        printf("%d", n);
    }

    for (int i = 0; i < n; ++i) {
        printf("Doing fork:\n");
        fork();
        printf("Sleeping: \n");
        sleep(5);
    }

	return EXIT_SUCCESS;

}
