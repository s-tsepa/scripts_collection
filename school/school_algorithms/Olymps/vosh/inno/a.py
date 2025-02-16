s = input()
n = int(input())


b = 'z'
ma = 'z'
flag = False
for x in 'abcdefghijklmnopqrstuvwsqz':
    if flag:
        break

    for i in range(len(s)):
        if s[i] == x:
            flag = True
            ma = x
            a1 = 'z'
            a2 = 'z'
            if i < (len(s) - 1):
                a1 = s[i + 1]
            if i > 0:
                a2 = s[i - 1]

            m = min(a1, a2)
            b = min(b, m)

    # break

print((ma + b) * (n // 2) + (ma if n % 2 == 1 else ''))
