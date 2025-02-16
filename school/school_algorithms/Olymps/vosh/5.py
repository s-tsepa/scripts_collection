n = int(input())

arr = [int(input()) for _ in range(n)]

p = [0 for _ in range(n)]
p[0] = arr[0]

for i in range(1, len(arr)):
    p[i] = p[i - 1] + arr[i]

# print(p)

for x in range(1, len(arr)):
    for y in range(x, len(arr) - 1):
        s1 = p[x - 1]
        s2 = p[y] - p[x - 1]
        s3 = p[-1] - p[y]

        if (s1 > 0 and s2 > 0) or (s2 > 0 and s3 > 0) or (s3 > 0 and s1 > 0):
            # print(x, y + 1, ': ', s1, s2, s3)
            x1 = x
            y1 = y + 1
            print(x1, y1 - x1, len(arr) - y1)
            exit()
print(0)
