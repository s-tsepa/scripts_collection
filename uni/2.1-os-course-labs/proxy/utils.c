//
// Created by void on 3/21/23.
//

#include "utils.h"

#include <errno.h>

#include <stdlib.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <string.h>
#include <stdio.h>

int log_func(int func_result, char* log_msg) {
    printf("%s: ", log_msg);

    if (func_result < 0) { // == -1
        fprintf(stderr, "FAILED (%d)\n", func_result);
        fprintf(stderr, "=== Error: %s ===", strerror(errno));
        return -1;
    } else {
        printf("OK (%d)\n", func_result);
        return func_result;
    }
}

void write_to_file(char* path, char* buff) {
    FILE* file = fopen(path, "w");
    fprintf(file, "%s", buff);

    printf("WRITING TO FILE: %s, LEN: %lu\n", path, strlen(buff));
    fclose(file);
}

int read_from_file(char* path, char* buff) {
    FILE* file = fopen(path, "rb");

    fseek(file, 0, SEEK_END); // seek to the end of the file
    int file_size = (int) ftell(file); // get the file size
    fseek(file, 0, SEEK_SET); // seek back to the beginning of the file

    int read_code = (int) fread(buff, sizeof(char), file_size, file);
    if (read_code < 0) { return -1; }

    printf("READ FROM FILE: %s, LEN: %d\n", path, file_size);
    fclose(file);
    return read_code;
}

int wait_interrupt(char* msg_print) {
    printf("%s", msg_print);
    char *q1 = malloc(sizeof(char) * 10);

    scanf("%s", q1);
    if (q1[0] == 'y') {
        return 1;
    } else {
        return 0;
    }
}


int get_server_port(int argn, char** argv) {
    if (argn > 1) {
        return (int) strtol(argv[1], NULL, 10);
    } else {
        printf("setting SERVER_PORT to default: %d\n", DEFAULT_SERVER_PORT);
        return DEFAULT_SERVER_PORT;
    }
}

void setup_server_addr(struct sockaddr_in* server_addr, int SERVER_PORT) {
    memset(server_addr, 0, sizeof(*server_addr));
    server_addr->sin_family = AF_INET;
    server_addr->sin_addr.s_addr = INADDR_ANY; // inet_addr(SERVER_IP_ADDR);
    server_addr->sin_port = htons(SERVER_PORT);
}


void print_sockfd_info(int sockfd) {
    struct sockaddr_in conn_addr;
    socklen_t addr_len = sizeof(conn_addr);
    getsockname(sockfd, (struct sockaddr *)&conn_addr, &addr_len);
    printf("===== %d =====\n", sockfd);
    printf("Socket address: %s\n", inet_ntoa(conn_addr.sin_addr));
    printf("Socket port: %d\n", ntohs(conn_addr.sin_port));
    printf("=====   =====\n");
}
