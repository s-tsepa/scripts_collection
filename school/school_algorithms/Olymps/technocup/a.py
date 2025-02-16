t = int(input())

def main(arr, n, k):

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(main(arr, n, k))

