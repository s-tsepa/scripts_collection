//
// Created by void on 3/21/23.
//

#ifndef C_UTILS_H
#define C_UTILS_H

#include <arpa/inet.h>

#define MESSAGE_SIZE 2048
#define DEFAULT_SERVER_PORT 2022

enum boolean { true, false };

extern int log_func(int func_result, char* log_msg);
extern void write_to_file(char* path, char* buf);
extern int read_from_file(char* path, char* buff);
extern int wait_interrupt(char* msg_print);
extern int get_server_port(int argn, char** argv);
extern void setup_server_addr(struct sockaddr_in* server_addr, int SERVER_PORT);
extern void print_sockfd_info(int sockfd);

#endif //C_UTILS_H
