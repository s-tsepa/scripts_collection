n = int(input())
k = int(input())


b = n + n + 1

r = 0
m = 0

# import pdb; pdb.set_trace()
if k > b:
    r += ((k -1) // b) * 2
    # k = k % b
    k -= (r // 2) * b

    if k > n:
        r += 1
        k -= n

    print(r + 1, k)
else:
    if k <= n:
        print(1, k)
    elif k > n:
        print(2, k - n)
