n = int(input())

def rs(x):
    return 2 ** (x ** 2)

# print(rs(n // 2))

def main(n):
    if n % 2 == 0:
        return rs(n // 2)
    else:
        # return rs(n // 2) + 2 ** (n // 2 + 1)
        return 0

print(main(n) % 1000000007)
