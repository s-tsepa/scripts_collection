def bp(arr, x):
    l = 0
    r = len(arr)

    if r - l == 1:
        return x == arr[0]

    while r - l > 1:
        m = (r + l) // 2

        if arr[m] < x:
            l = m

        elif arr[m] == x or r == x:
            return True

        else:
            r = m
    #
    # if r != len(arr) and l != -1:
    #     return True

    if arr[l] == x or arr[r -1] == x:
        return True

    return False


n, k = list(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


for i in arr2:
    if bp(arr1, i):
        print("YES")
    else:
        print("NO")

