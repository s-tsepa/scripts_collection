ans = []
def f(s):
    a = (int(s[0]) * 10 + int(s[1])) ** 2
    b = (int(s[2]) * 10 + int(s[3])) ** 2
    # print(a, b)
    if ((a + b) % 7 == 1):
        ans.append("YES")
    else:
        ans.append("NO")

for i in range(int(input())):
    f(input())

for i in ans:
    print(i)