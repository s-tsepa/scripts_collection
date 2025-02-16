n, m = list(map(int, input().split()))

arr = [0] + list(map(int, input().split()))

dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

dp[0][0] = True



for i in range(1, n + 1):
    for j in range(0, m + 1):
        dp[i][j] = dp[i - 1][j]
        if arr[i] <= j and dp[i - 1][j - arr[i]]:
            dp[i][j] = True
            if j == m:
                print("YES")
                exit()

print("NO")
