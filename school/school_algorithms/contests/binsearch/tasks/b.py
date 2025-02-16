def bp(arr, x):
    l = 0
    r = len(arr) - 1

    # if r - l == 1:
    #     return x == arr[0]

    for _ in range(20):
        m = (r + l) // 2

        if arr[m] > x:
            r = m
        #
        # elif arr[m] == x or r == x:
        #     return True

        else:
            l = m

    # return l, r

    if r != l:
        if abs(arr[r] - x) < abs(arr[l] - x):
            return r

    return l

n, k = list(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for j in range(len(arr2)):

    print(arr1[bp(arr1, arr2[j])])

