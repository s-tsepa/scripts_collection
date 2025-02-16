

CFLAGS = -Wall -Werror
#CFLAGS = -Wall
BUILD_DIR = build
CLIENT_DIR = client
SERVER_DIR = server
BIN_DIR = bin

SRCS_CLIENT = $(CLIENT_DIR)/client.c lib_tcp.c utils.c
OBJS_CLIENT = $(SRCS_CLIENT:%.c=$(BUILD_DIR)/%.o)

SRCS_SERVER = $(SERVER_DIR)/server.c lib_tcp.c utils.c
OBJS_SERVER = $(SRCS_SERVER:%.c=$(BUILD_DIR)/%.o)


OUT_CLIENT = $(BIN_DIR)/client
OUT_SERVER = $(BIN_DIR)/server

all: clean build_client build_server

build_client: $(OBJS_CLIENT)
	$(info --- $@ ---)

	$(eval OUT = $(BUILD_DIR)/$(OUT_CLIENT))
	mkdir -p $(dir $(OUT))
	gcc $(CFLAGS) $^ -o $(OUT)

build_server: $(OBJS_SERVER)
	$(info --- $@ ---)

	$(eval OUT = $(BUILD_DIR)/$(OUT_CLIENT))
	mkdir -p $(dir $(OUT))
	gcc $(CFLAGS) $^ -o $(BUILD_DIR)/$(OUT_SERVER)

$(BUILD_DIR)/%.o: %.c
	mkdir -p $(@D)
	gcc $(CFLAGS) $< -c -o $@

clean:
	rm -rvf $(BUILD_DIR)
#	mkdir $(BUILD_DIR)
#	mkdir $(BUILD_DIR)/$BIN_DIR
#	mkdir $(BUILD_DIR)/$(CLIENT_DIR)

