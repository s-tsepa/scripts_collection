def getSquare(x):
    return a * (x ** 3) + b * (x ** 2) + c * x + d


def bp():

    r = 1
    while (getSquare(r) * getSquare(-r) >= 0):
        r *= 2

    l = -r;

    while r - l > 10 ** -12:

        m = (l + r) / 2

        n = getSquare(m)
        n2 = getSquare(r)

        if n * n2 <= 0:
            l = m
        else:
            r = m
    return l


a, b, c, d = list(map(int, input().split()))

ans = bp()

print(round(ans, 4))
