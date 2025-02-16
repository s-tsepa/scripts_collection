n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

q = int(input())
for i in range(q):
    t, l, r = map(int, input().split())
    for _ in range(r - l + 1):
        if t == 1:
            b.append(a.pop(l - 1))
        elif t == 2:
            a.append(b.pop(l - 1))
    a.sort()
    b.sort()

    # print()
    # print(a, b)

print(len(a))
print(*a)
print(len(b))
print(*b)

