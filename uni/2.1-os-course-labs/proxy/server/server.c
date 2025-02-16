//
// Created by void on 3/21/23.
//


#include "../lib_tcp.h"
#include "../utils.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <pthread.h>
#include <signal.h>

#define MAX_CLIENTS 5
#define DEFAULT_RESP_FILENAME "assets/default_resp.txt"

pthread_mutex_t send_lock;
pthread_mutex_t recv_lock;

int SERVER_PORT;
int accepting_socket_fd;
struct sockaddr_in server_addr;
char client_msg_buf[MESSAGE_SIZE];
char resp_buf[MESSAGE_SIZE];

void* server_main(void* arg) {
    int conn_socket_fd = *(int*) arg;

    pthread_mutex_lock(&recv_lock);
    bzero(client_msg_buf, MESSAGE_SIZE);
    int recv_code = recv_single(conn_socket_fd, client_msg_buf, MESSAGE_SIZE);
    pthread_mutex_unlock(&recv_lock);

    if (log_func(recv_code, "Receiving SINGLE") < 0) return (void *) -1;

    printf("RECV:\n\n%s\n", client_msg_buf);

    pthread_mutex_lock(&send_lock);

    /* sprintf(resp_buf, svg_template, client_msg_buf); */
    int read_code = read_from_file(DEFAULT_RESP_FILENAME, resp_buf);
    if (read_code == -1) { return (void *) -1; }

    send_message(conn_socket_fd, resp_buf);
    memset(resp_buf, '\0', sizeof(resp_buf));

    pthread_mutex_unlock(&send_lock);

    printf("Closing CONNECTION socket: (%d)\n============\n", conn_socket_fd);
    close(conn_socket_fd);

    return (void *) 0;
}

void handle_ctrl_c(int sig) {
    printf("\nClosing ACCEPTING socket: (%d)\n", accepting_socket_fd);
    close(accepting_socket_fd);
//    pthread_exit(NULL);
    exit(EXIT_SUCCESS);
}

int main(int argn, char** argv) {
    signal(SIGINT, handle_ctrl_c);

    SERVER_PORT = get_server_port(argn, argv);

    // === CREATE ACCEPING SOCKET ===
    accepting_socket_fd = create_tcp_socket_fd();
    if (log_func(accepting_socket_fd, "Create ACCEPTING socket") < 0) exit(EXIT_FAILURE);

    // === BIND SOCKET TO HOST:PORT
    setup_server_addr(&server_addr, SERVER_PORT);
    int bind_code = bind_socket(accepting_socket_fd, &server_addr);
    if (log_func(bind_code, "BIND socket") < 0) exit(EXIT_FAILURE);

    print_sockfd_info(accepting_socket_fd);

    // === LISTEN ===
    int listen_code = listen(accepting_socket_fd, MAX_CLIENTS);
    if (log_func(listen_code, "LISTENING") < 0) exit(EXIT_FAILURE);

    printf("=== Server is listening on \"%s:%d\" ===\n", SERVER_IP_ADDR, SERVER_PORT);

    // === ACCEPT (CREATE CONNECTION SOCKET) ===
    struct sockaddr client_addr;
    while (1) {
        int conn_socket_fd = accept_conn(accepting_socket_fd, &client_addr);
        printf("\n\n");
        if (log_func(listen_code, "Create CONNECTION socket") < 0) exit(EXIT_FAILURE);
        print_sockfd_info(conn_socket_fd);

        // === PTHREAD CREATE ===
        pthread_t tid;
        int pthread_code = pthread_create(&tid, NULL, server_main, (void *)&conn_socket_fd);
        if (log_func(pthread_code, "PTHREAD create") != 0) break;
    }
}
