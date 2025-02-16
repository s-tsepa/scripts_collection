n = int(input())
a = list(map(int, input().split()))

m = int(input())

b = list(map(int, input().split()))

dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if a[i - 1] == b[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

ans = []
i = len(a)
j = len(b)
while i > 0 and j > 0:
    if a[i - 1] == b[j - 1]:
        ans.append(a[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] == dp[i][j]:
        i -= 1
    else:
        j -= 1

print(*list(reversed(ans)))
