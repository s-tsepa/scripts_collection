
from operator import *
n = int(input())

d = dict()
arr = []
names = []

for i in range(n):
    s = input().split()
    for j in range(3):
        if s[j] not in d:
            if j == 2:
                continue
            d[s[j]] = 1
        elif j != 2:
            # s.reverse()
            names.append(s[j])
            d[s[j]] += 1
        else:
            d[s[j]] += 1
    arr.append(s)

for i in range(n):
    for name in names:
        if name in arr[i]:
            if arr[i][0] == name:
                arr[i] = [arr[i][-1], arr[i][0], arr[i][1]]

arr.sort(key=itemgetter(0, 1, 2))

for i in range(n):
    print(*arr[i])