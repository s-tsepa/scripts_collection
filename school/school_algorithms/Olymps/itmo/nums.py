def cv(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return cv(n // to_base, to_base) + alphabet[n % to_base]

d = int(input())
l = int(input())
n = input()

i = 0
while n[i] == '0' and i < l - 1:
    i += 1
n = n[i:]
# print(n)

# print(cv('ABCDEF', 8, 16))

n2 = str(cv(n, 8, 16))
# print('n2', n2)
print(n2.count(str(d)))
