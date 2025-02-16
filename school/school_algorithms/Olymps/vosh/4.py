n = int(input())
m = int(input())

r = sorted([int(input()) for _ in range(n)])
l = [int(input()) for _ in range(m)]
l.sort(reverse=True)

# prev = float('inf')
# cur = 0

# while cur < prev:
#     cur = sum(p) + sum(o)

b1 = 0
b2 = 0
m1 = 0
m2 = 0

for i in r:
    if i < 0:
        m1 += 1
    if i >= 0:
        b1 += 1

for i in l:
    if i <= 0:
        m2 += 1
    if i > 0:
        b2 += 1

d = b1 + m2 - m1 - b2

if d > 0:
    print(0)
    exit()

t = 0

for i in range(len(r)):
    if r[i] > 0:
        r = r[:i]
        break
    else:
        r[i] = -r[i]

for i in range(len(l)):
    if l[i] < 0:
        l = l[:i]
        break


res = l + r
res.sort()
# print(res)
nested = 0

while d < 0:
    if nested > 0:
        d += nested
        nested = 0
    print(res, d)
    t += res[0]
    d += res[0]
    res = list(map(lambda x: x - res[0], res))
    res.pop(0)
    nested += 1
    # print(res)

print(t)
