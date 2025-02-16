n = int(input())

arr = list(map(int, input().split()))


def insert_sort(arr, n):
    for i in range(n - 1):
        j = n - 1
        while j > i:
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

            j -= 1

    return arr


print(*insert_sort(arr, n))
