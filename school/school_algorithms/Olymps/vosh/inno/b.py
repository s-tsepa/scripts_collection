n = int(input())
arr = list(map(int, input().split()))

def pp(arr):
    def p(arr):
        for i in range(len(arr)):
            yield [arr[i], i]
    return list(p(arr))

arr = pp(arr)
    
s = sorted(arr, key=lambda x: x[0])

def get(arr, n):
    for i in range(len(arr)):
        if arr[i][0] == n:
            yield i

res = []

frozen = set()

import pdb
for i in range(len(arr)):
    # pdb.set_trace()
    if i in frozen:
        continue
    x, j = arr[i]
    y, q = s[i]

    if x == y:
        continue

    ns = list(map(lambda ind: ind + j, get(arr[j:], y)))
    if len(ns) == 1:
        if s[q][0] == x:
            # if j <= q:
            res.append((j, q))
            arr[j], arr[q] = arr[q], arr[j]
            frozen.add(q)
            frozen.add(j)
        else:
            print('No')
            exit()
    else:
        for z in ns:
            if s[z][0] == x:
                # if j <= z:
                res.append((j, z))
                arr[j], arr[z] = arr[z], arr[j]
                frozen.add(z)
                frozen.add(j)
                break
        else:
            print('No')
            exit()


def pr(res):
    for i in res:
        a, b = i
        if a != b:
            yield a, b

r = list(pr(res))
# if len(r) == 0:
#     print('No')
#     exit()
print('Yes')
print(len(r))
print('\n'.join(list(map(lambda x: f'{x[0] + 1} {x[1] + 1}', r))))
