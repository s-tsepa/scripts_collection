def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def factor(n):
   Ans = []
   d = 2
   while d * d <= n:
       if n % d == 0:
           Ans.append(d)
           n //= d
       else:
           d += 1
   if n > 1:
       Ans.append(n)
   return Ans

q = []

def rec(arr, n):
    if n == 0:
        q.append(arr)
    else:
        rec(arr + [0], n - 1)
        rec(arr + [1], n - 1)

a, b = [int(s) for s in input().split()]

if (a != b):
    NOD = gcd(a, b)
    NOK = a * b // NOD
    pr = factor(a // NOD) + factor(b // NOD)
    prime = []
    last, nom = pr[0], 1
    for i in range(1, len(pr)):
        if last == pr[i]:
            nom += 1
        else:
            prime.append([last, nom])
            nom = 1
            last = pr[i]
    prime.append([last, nom])
    ans = [min(a, b), max(a, b)]
    rec([], len(prime))
    for j in range(len(q)):
        chi = NOD
        for i in range(len(prime)):
            if (q[j][i]):
                chi *= prime[i][0] ** prime[i][1]
        if (abs(a * b // chi - chi) < abs(ans[1] - ans[0])):
            ans = sorted([a * b // chi, chi])

    print(*ans)
else:
    print(a, b)