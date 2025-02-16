n = int(input())
n -= 1

if n == 0:
    print()
    exit()


dp = [float("inf")] * (n + 1)
# seq = [[]] * (n + 1)
ans = []

dp[0] = 0
dp[1] = 0



for i in range(1, n):
    op = dp[i] + 1

    if op < dp[i + 1]:
        dp[i + 1] = op
        # seq[i + 1] = seq[i] + [1]

    if i * 2 < n + 1:
        if op < dp[i * 2]:
            dp[i * 2] = op
            # seq[i * 2] = seq[i] + [2]

    if i * 3 < n + 1:
        if op < dp[i * 3]:
            dp[i * 3] = op
            # seq[i * 3] = seq[i] + [3]

i = n + 1
while i > 1:
    dell = [dp[i - 1], float("inf"), float("inf")]

    if i % 3 == 0:
        dell[2] = dp[i // 3]
    if i % 2 == 0:
        dell[1] = dp[i // 2]

    if dell[0] == min(dell):
        ans.append(1)
        i -= 1
    else:
        if dell[1] == min(dell):
            ans.append(2)
            i //= 2
        elif dell[2] == min(dell):
            ans.append(3)
            i //= 3

ans.reverse()
print("".join(map(str, ans)))
