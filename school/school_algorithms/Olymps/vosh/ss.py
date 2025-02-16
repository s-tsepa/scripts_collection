N = int(input())
K = int(input())

a = None
b = K

if K <= N:
    print(K)
else:
    if K / N > K // N:
        a = K // N + 1
    else:
        a = K / N

while b >= 10:
    if b > 10:
        b -= N
    if b > 10:
    b -= N + 1
