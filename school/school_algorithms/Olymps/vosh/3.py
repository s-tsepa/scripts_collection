import random, string

def randomword(length):
   letters = string.printable
   return ''.join(random.choice(letters) for i in range(length))

# t = input()
# s = input()
# n = int(input())

# print((s * n).count(t))

# s *= 3
# cnt = 0
# for i, x in enumerate(s):
#     if 

def main(t, s, n):
    cnt = 0
    s *= n
    for i in range(len(s)):
        # print(s[i:len(t) + i])
        if s[i:len(t) + i] == t:
            cnt += 1
    return cnt

for _ in range(10 ** 10):
    t = randomword(random.randint(1, 50))
    s = randomword(random.randint(1, 100))
    n = random.randint(1, 100)

    print(t, s, n, main(t, s, n))

