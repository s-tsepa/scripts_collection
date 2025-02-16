x = int(input())
y = int(input())

if x * y < 0:
    if y < 0:
        if x < -y:
            print(2)
            print(x, x, 'H')
            y1 = (x - y) // 2
            print(x + y1, x - y1, 'V')
            exit()
    if x < 0:
        if y < -x:
            print(2)
            print(y, y, 'V')
            x1 = (y - x) // 2
            print(y + x1, y - x1, 'H')
            exit()

if x == y:
    print(0)
    exit()

if (x + y) % 2 != 0:
    print(-1)
    exit()

print(1)
r = (x + y) // 2

if x > y:
    print(r, r, 'H')
elif x < y:
    print(r, r, 'V')
