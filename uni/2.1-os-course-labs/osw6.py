import pprint
import queue

arr = [list(map(int, input().split())) for _ in range(3)]

arr.sort(key=lambda x: x[0])  # by arrive time

pprint.pprint(arr)

cur_tick = 0  # arr[0][0]
sum_compl_time = 0
sum_tat_time = 0

for i in range(len(arr)):
    at, bt = arr[i]

    if cur_tick < at:
        cur_tick = at

    waiting_time = cur_tick - at
    print(f'Waiting time for {i} proc: {waiting_time}')

    # cur_tick = at
    cur_tick += bt

    print(f'Completion time for {i} proc: {cur_tick}')
    print(f'TAT for {i} proc: {bt}')
