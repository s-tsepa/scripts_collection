//
// Created by void on 3/20/23.
//

#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#include "lib_tcp.h"
#include "utils.h"

int accept_conn(int accepting_socket_fd, struct sockaddr* client_addr) {
    int addr_len = sizeof(&client_addr);

    int conn_socket_fd = accept(accepting_socket_fd, client_addr, (socklen_t*) &addr_len);
    return conn_socket_fd;
}

int bind_socket(int socket_fd, struct sockaddr_in* server_addr) {
    int server_addr_size = sizeof(*server_addr);

    int bind_code = bind(socket_fd, (struct sockaddr*) server_addr, server_addr_size);
    return bind_code;
}

int create_tcp_socket_fd() {
    int result = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    return result;
}

int send_message(int socket_fd, char *buf) {
    size_t msg_len = strlen(buf);

    int send_result = (int) send(socket_fd, buf, msg_len, 0);
    return send_result;
}

int recv_single(int socket_fd, char* buf, int size) {
    int recv_result = (int) recv(socket_fd, buf, size, 0);
    return recv_result;
}

int recv_available(int socket_fd, char* buf, int max_size) {
    char* cur_buf_ptr;
    int recv_total_bytes = 0;

    while (recv_total_bytes < max_size) {
        cur_buf_ptr = buf + recv_total_bytes;

        int new_bytes = recv_single(socket_fd, cur_buf_ptr, max_size);
        if (log_func(new_bytes, "Receiving SINGLE") < 0) return -1;

        recv_total_bytes += new_bytes;
        if (new_bytes == 0) { break; }
    }
    return recv_total_bytes;
}

int connect_to_addr(int socket_fd, struct sockaddr_in server_addr) {
    int server_addr_size = sizeof(server_addr);
    int conn_result = connect(socket_fd, (const struct sockaddr *) &server_addr, server_addr_size);

    if (conn_result != 0) {
        return -1;
    } else {
        return 0;
    }
}


