n = int(input())

arr = list(map(int, input().split()))


def min_sort(arr, n):
    for i in range(n - 1):
        for j in range(i, n):

            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(*min_sort(arr, n))

