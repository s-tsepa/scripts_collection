n = int(input())

arr = list(map(int, input().split())) 

ans = []

for i in range(min(n, arr[0])):
    if i < arr[i]:
        ans.append([i + 1, i + 1])
    else:
        break
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])