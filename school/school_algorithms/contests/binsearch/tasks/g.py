n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))


def bp():
    l = 0
    r = arr[-1]#len(arr)

    maxK = 0

    while r - l > 1:
        m = (l + r) // 2

        if can(m):
            l = m
            # print(m)
            maxK = max(m, maxK)

        else:
            r = m

    return maxK
    # return l, r, m, maxK


def can(x):
    ans = 1
    prev = 0

    for i in range(1, n):
        if arr[i] - arr[prev] >= x:
            prev = i
            ans += 1

    if ans >= k:
        return True

    else:
        return False


print(bp())
