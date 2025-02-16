def main():
    stack = []

    def hn(s):
        return any(char.isdigit() for char in s)

    def aton(s):
        st = 0
        res = 0
        for i in reversed(list(s)):
            if i == 'A':
                res += -1 * 5 ** st
            elif i == 'B':
                res += -2 * 5 ** st
            else:
                res += int(i) * 5 ** st
            st += 1

        return res
    sd = '*+-/'

    a = list(input())
    for i, k in enumerate(a):
        if i == 0:
            continue
        if k.isdigit() and a[i - 1] in sd or a[i - 1].isdigit() and k in sd:
            a.insert(i, ' ')

    # print('a', a)
    a = ''.join(a).split()
    # print('a', a)

    res = []
    for i in a:
        if any(char in '*+-/' for char in i):
            # if i[0].isdigit():
                # for j, t in enumerate(i):
                #     if t in '*+-/':
                #         ll = list(i)
                #         ll.insert(j, ' ')
            res.extend(list(i))
        else:
            res.append(float(i))

    # print('res', res)

    try:
        for i in res:
            if isinstance(i, str):
                b, a = stack.pop(), stack.pop()
                if i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(a / b)
                elif i == '+':
                    stack.append(a + b)
                else:
                    stack.append(a - b)
            else:
                stack.append(i)

            # print(stack)
    except Exception as e:
        # print(e)
        print('ERROR')
        return

    if len(stack) != 1:
        print('ERROR')
        return

    r = stack[0]
    # print('r', r)
    # print('rround', round(r, 11))
    r = round(r, 11)
    f1, f2 = str(r).split('.')
    # print(f1, f2)
    if len(str(f1)) > 16:
        print('ERROR')
        return
    print('0' * (16 - len(str(f1))), f1, f2, '0' * (11 - len(str(f2))), sep='')

main()
