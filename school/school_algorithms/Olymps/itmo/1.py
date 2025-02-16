a = int(input())
b = int(input())

c1 = a // 3
c2 = b // 3
c3 = 0

a = a % 3
b = b % 3

while a > 0 and b > 0:
    b -= 1
    a -= 1
    c3 += 1

if a != 0 or b != 0:
    print(-1)
    exit()
else:
    print(c1, c3, c2)
