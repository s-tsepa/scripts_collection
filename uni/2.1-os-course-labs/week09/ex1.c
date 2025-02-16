#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define AGING_BITS 8
#define MAX_COUNTER_INT 1 << (AGING_BITS + 1)

typedef struct VirtualPage{
    int number;
    char counter_bits_string[AGING_BITS + 1];
    int counter;
    int r_bit;
    int is_present;
} t_data;


void age_page(struct VirtualPage* vp) {
    int len = strlen(vp->counter_bits_string);
    char new_bit = vp->r_bit + '0';

    for (int i = len - 1; i >= 1; --i) {
        vp->counter_bits_string[i] = vp->counter_bits_string[i - 1];
    }
    vp->counter_bits_string[0] = new_bit;
//    vp->counter_bits_string[len] = '\0';


    vp->counter = (int) strtol(vp->counter_bits_string, NULL, 2);
//    if (vp->counter != 0) {
//        printf("%d %s %d\n", vp->number, vp->counter_bits_string, vp->counter);
//    }
}

void func(int page_frames_count) {
    int hits = 0, misses = 0;
    struct VirtualPage* virtual_mem_pages[1024];


    for (int i = 0; i < 1024; ++i) {
        t_data *vp;
        vp = malloc(sizeof(t_data));
        vp->number = i;
        vp->counter = 0;
        vp->r_bit = 0;
        vp->is_present = 0;
//        vp->counter_bits_string[0] = '0';
        for (int j = 0; j < AGING_BITS; ++j) {
            vp->counter_bits_string[j] = '0';
        }
        vp->counter_bits_string[AGING_BITS] = '\0';
        virtual_mem_pages[i] = vp;
    }

    int n;
    FILE * f = fopen("input.txt", "r");
    while (fscanf(f, "%d", &n) == 1) {
        int found_flag = 0;

        struct VirtualPage* present_pages[1024];
        int present_cnt = 0;

        for (int i = 0; i < 1024; ++i) {
            // reset all R bits to "0", and do aging for all counter values
            age_page(virtual_mem_pages[i]);
            virtual_mem_pages[i]->r_bit = 0;

            // Form an array of pages present in physical memory
            if (virtual_mem_pages[i]->is_present) {
                present_pages[present_cnt] = virtual_mem_pages[i];
                present_cnt++;

                // Found page on physical memory
                if (i == n) {
                    hits++;
                    virtual_mem_pages[n]->r_bit = 1;
                    found_flag = 1;
                }
            }
        }

        if (found_flag == 1) { continue; }
        misses++;

        // If there is not enough memory to load new page
        if (present_cnt >= page_frames_count) {
            // Select worst page to remove in terms of aging algo
            int min_counter_bits = MAX_COUNTER_INT;
            struct VirtualPage* remove_candidate = present_pages[0];
            for (int i = 0; i < present_cnt; ++i) {
                if (present_pages[i]->counter < min_counter_bits) {
                    min_counter_bits = present_pages[i]->counter;
                    remove_candidate = present_pages[i];
                }
            }

            remove_candidate->is_present = 0;
        }

        virtual_mem_pages[n]->is_present = 1;
        virtual_mem_pages[n]->r_bit = 1;

    }
    printf("For %d: %d %d %f\n", page_frames_count, hits, misses, (float) hits/ (float) misses);
}


int main() {
//    int page_frames_count;
//    scanf("%d", &page_frames_count);

    func(5);
    func(10);
    func(50);
    func(100);
}
