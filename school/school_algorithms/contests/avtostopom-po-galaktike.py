import sys

sys.setrecursionlimit(10**5)

def dfs(start, c, graph, cache):
    vis = 0

    if c != start:
        vis |= 1 << c

    for i in graph[c]:
        vis |= 1 << i
        vis |= cache[i]
    return vis


def main():
    n = int(input())
    graph1 = [[] for _ in range(n)]
    graph2 = [[] for _ in range(n)]

    for i in range(n - 1):
        s = input()
        for j in range(len(s)):
            if s[j] == "B":
                graph1[i].append(i + j + 1)
            else:
                graph2[i].append(i + j + 1)

    cache1 = {}
    cache2 = {}

    for i in reversed(range(n)):
        cache1[i] = dfs(i, i, graph1, cache1)

    for i in reversed(range(n)):
        cache2[i] = dfs(i, i, graph2, cache2)
        if cache1[i] & cache2[i]:
            return "NO"

    return "YES"


print(main())
