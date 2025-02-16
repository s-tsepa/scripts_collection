def dijkstra(n, S, matrix):
        valid = [True] * n
        weight = [100 ** 2] * n
        weight[S] = 0
        for i in range(n):
                min_weight = 100 ** 2 + 1
                ID_min_weight = -1
                for i in range(len(weight)):
                        if valid[i] and weight[i] < min_weight:
                                min_weight = weight[i]
                                ID_min_weight = i
                for i in range(n):
                        if matrix[ID_min_weight][i] == -1:
                                continue
                        if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
                valid[ID_min_weight] = False
        return weight

n, s, f = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
    
x = dijkstra(n, s - 1, arr)#[f - 1]

if x[f - 1] == 100 ** 2:
    print(-1)
    exit()

print(x[f - 1])

