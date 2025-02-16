n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

def f(arr, a, b):
    ma = 0

    for i in range(a, b):
        if arr[i] > arr[ma]:
            ma = i

    return ma

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:# and dp[j] > dp[i]:
            #dp[i] = dp[j]
            dp[i] = max(dp[i], 1 + dp[j])

print(max(dp))

