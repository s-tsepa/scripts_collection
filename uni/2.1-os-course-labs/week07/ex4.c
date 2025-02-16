#include <stdlib.h>
#include <memory.h>

void* my_realloc(void *ptr, size_t size1, size_t size2) {

    if (!ptr) { return malloc(newSize); }
    if (size2 == 0) {
        free(ptr);
        return NULL;
    }

    void *ptr2 = malloc(size2);
    memcpy(ptr2, ptr, size1);
    free(ptr);

    return ptr2;
}
