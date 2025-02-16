from math import *

b, a = list(map(int, input().split()))
y = float(input())

def f(x, y):
    s1 = sqrt(1 - 2 * x + x ** 2 + y ** 2)
    s2 = sqrt(1 - 2 * y + y ** 2 + x ** 2)
    t = s1 / a + s2 / b
    return t

def bp():
    l = 0
    r = 1
    while r - l > 1e-9:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3


        if (f(m1, y) > f(m2, y)):
            l = m1
        else:
            r = m2
    return l

print(round(bp(), 6))
