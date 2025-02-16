def getSum(x):
    return x ** 2 + x ** 0.5

def bp(c):
    l = 0
    r = 10 ** 10
    while r - l > 10 ** -10:

        m = (l + r) / 2

        n = getSum(m)
        if n < c:
            l = m
        else:
            r = m
    return r

c = float(input())

ans = bp(c)


print(round(ans, 6))