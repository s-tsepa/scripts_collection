//
// Created by void on 3/20/23.
//

#ifndef C_LIB_TCP_H
#define C_LIB_TCP_H

#include <arpa/inet.h>

#define SERVER_IP_ADDR "127.0.0.1"

extern int create_tcp_socket_fd();
extern int accept_conn(int accepting_socket_fd, struct sockaddr* client_addr);
extern int bind_socket(int socket_fd, struct sockaddr_in* server_addr);
extern int send_message(int socket_fd, char *buf);
extern int recv_single(int socket_fd, char* buf, int size);
extern int recv_available(int socket_fd, char* buf, int max_size);
extern int connect_to_addr(int socket_fd, struct sockaddr_in server_addr);

#endif //C_LIB_TCP_H
