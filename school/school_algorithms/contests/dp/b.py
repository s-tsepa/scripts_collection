def f(a, i, j, n):
    while i < n and j >= 0:
        a[i][j] += a[i - 2][j - 1] + a[i - 1][j - 2] + a[i - 2][j + 1] + dp[i + 1][j - 2]
        i += 1
        j -= 1
 
 
n, m = map(int, input().split())
dp = [[0 for j in range(m + 2)] for i in range(n + 2)]
dp[0][0] = 1
 
for j in range(m):
    f(dp, 0, j, n)
 
for i in range(1, n):
    f(dp, i, m - 1, n)
 
# for i in range(n):
#     print(*dp[i])
print(dp[n - 1][m - 1])