n = int(input())

arr = list(map(int, input().split()))

shift = min(arr)

if shift < 0:
    shift *= -1
else:
    shift = 0

counts = [0 for i in range(max(arr) + shift + 1)]

for num in arr:
    num += shift

    counts[num] += 1

res = []

for i in range(len(counts)):
    p = [i - shift for _ in range(counts[i])]
    res += p

#print(counts)
print(*res)
