n = int(input())

arr = list(map(int, input().split()))

amax = max(arr)
amin = min(arr)

arr += [amax + 1]
n += 1

cnt = 0
cur = 0

# import pdb; pdb.set_trace()

cur += amax - arr[0]

for i in range(1, n):
    if arr[i] < arr[i - 1]:
        cur += arr[i - 1] - arr[i]
    elif arr[i] > arr[i - 1]:
        r = arr[i] - arr[i - 1]
        cur -= r
        cnt += r

print(cnt - 1)

# for i in range(amin + 1, amax + 1):
#     for j in range(n):
#         if j == 0:
#             continue

#         if arr[j] >= i and arr[j - 1] < i:
#             c += 1

#         if j == n - 1 and arr[j] < i:
#             c += 1

# print(c)
