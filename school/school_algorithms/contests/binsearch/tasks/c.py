def rbp(arr, x):
    l = 0
    r = len(arr)

    if arr[-1] == x:
        return len(arr) - 1

    while r - l > 1:
        m = (r + l) // 2

        if arr[m] <= x:
            l = m
        else:
            r = m

    return l


def lbp(arr, x):
    l = 0
    r = len(arr)

    if arr[0] == x:
        return 0

    while r - l > 1:
        m = (r + l) // 2

        if arr[m] < x:
            l = m

        else:
            r = m

    return r

res = []

n = int(input())
arr = list(map(int, input().split()))

arr.sort()


m = int(input())
arr2 = list(map(int, input().split()))

for i in range(m):
    x = arr2[i]

    ans = rbp(arr, x) - lbp(arr, x) + 1

    res.append(ans)

print(*res)
# print(arr)
# print(lbp(arr, 1), rbp(arr, 1))
