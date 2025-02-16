def merge(arr, l, m, r):
    it1 = 0
    it2 = 0
    res = [0 for _ in range(r - l)]

    while l + it1 < m and m + it2 < r:
        if arr[l + it1] < arr[m + it2]:
            res[it1 + it2] = arr[l + it1]
            it1 += 1
        else:
            res[it1 + it2] = arr[m + it2]
            it2 += 1

    while l + it1 < m:
        res[it1 + it2] = arr[l + it1]
        it1 += 1

    while m + it2 < r:
        res[it1 + it2] = arr[m + it2]
        it2 += 1

    for i in range(it1 + it2):
        arr[l + i] = res[i]


def merge_sort(arr, l, r):
    if l + 1 >= r:
        return

    mid = (l + r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid, r)
    merge(arr, l, mid, r)

n = int(input())
arr = list(map(int, input().split()))

l = 0
r = n

merge_sort(arr, l, r)

print(*arr)
