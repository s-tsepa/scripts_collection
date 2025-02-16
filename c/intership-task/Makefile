

CFLAGS = -Wall -Werror
#CFLAGS = -Wall
BUILD_DIR = build
BIN_DIR = bin

OUT= $(BIN_DIR)/main_exec

all: clean build

build: $(BUILD_DIR)/main.o
	mkdir -p $(dir $(OUT))
	gcc $(CFLAGS) $^ -o $(OUT)

$(BUILD_DIR)/%.o: %.c
	mkdir -p $(@D)
	gcc $(CFLAGS) $< -c -o $@

clean:
	rm -rvf $(BUILD_DIR)

