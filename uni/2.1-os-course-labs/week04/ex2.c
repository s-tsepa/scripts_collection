#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

// <WRITE YOUR CODE HERE>


// Calculate the dot product of the vectors u and v from the component [start] till the component [end] exclusively.
int dotprod(int u[], int v[], int start, int end){

	int result = 0;
	
	for (int i=start; i<end; i++){
		result += u[i] * v[i];
	}
	
	return result;
}

int writeToFile(int x) {
    FILE * f;
    f = fopen("./temp.txt", "a");

    if (f != NULL) {
        char str[100];
        sprintf(str, "%d", x);
        strcat(str, "\n");
        fputs(str, f);
        fclose(f);
    }
}


int main(void){

    int n, k = 120;
    scanf("%d", &n);
//    n = ;

//    pid_t proc[n];
    int arr1[k];
    int arr2[k];

    for (int i = 0; i < k; ++i) {
//        arr1[i] = (rand() % 100);
//        arr2[i] = (rand() % 100);
        arr1[i] = i + 1;
        arr2[i] = i + 2;
    }

//    for (int i = 0; i < n; ++i) {
//        proc[i] = 0;
//    }

    int res_prod = 0;

    int range = k / n;

    int main_pid = getpid();
    int main_ppid = getppid();

    for (int i = 0; i < n; i++) {
        pid_t f = fork();

        if (getpid() == getpgid(f)) {
            int r = dotprod(arr1, arr2, range * i, range * (i + 1));
            writeToFile(r);
        }
    }

//    printf("PIDs: %d %d\n", getpid(), getppid());
    if (getpid() == main_pid) {
        FILE * f;
        char * line = NULL;
        size_t len = 0;
        int res = 0;

        f = fopen("./temp.txt", "r");
        if (f == NULL)
            exit(EXIT_FAILURE);

        while (getline(&line, &len, f) != -1) {
            int x;
            sscanf(line, "%d", &x);
            res += x;
        }

        fclose(f);
        if (line)
            free(line);
        printf("End: %d\n", res);
    }
	return EXIT_SUCCESS;

}

/*

Example:

Assume that
u = [u1, u2, u3, u4]
v = [v1, v2, v3, v4]pid_t ptemp = fork();
k=1 ==> n = 2 processes

Equally distribute the dot product calculation task. We have multiple ways to distribute the task equally.

1- A possible task distribution is as follows:

First process will calculate dot product for the first two components
Second process will calculate dot product for the last two components

The computation result of the first process is u1 * v1 + u2 * v2 ==> c1
The computation result of the second process is u3 * v3 + u4 * v4 ==> c2

2- Another possible distribution is as follows:

First process will calculate dot product for the even components
Second process will calculate dot product for the odd components

The computation result of the first process is u2 * v2 + u4 * v4 ==> c1
The computation result of the second process is u1 * v1 + u3 * v3 ==> c2



The file temp.txt will contain as follows: (format is not restricted)
-------------------
c1
c2
-------------------

The "main" process will aggregate all dot product computations of its children
It will read the lines and aggregate.

c1 + c2 ==> result of u * v


*/
