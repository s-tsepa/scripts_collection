fin = open('words.txt')
words = list(map(str.strip, fin.readlines()))

nodes = dict({0: ''})


# tree = [
#     [1, 2, 3] # 0 " "
#     [0, 2, 3] # 1
#     [0, 1], # 2
#     [0, 1] # 3
# ]

d = {
    "a": ["b", "c", "d"]
    "b": ["a", "c", "d"]
    "a": ["b", "c", "d"]
    "a": ["b", "c", "d"]
    "a": ["b", "c", "d"]
    "a": ["b", "c", "d"]
}

tree = [[0] for _ in range(27)]
tree[0] = [i for i in range(1, 27)]

print(tree)

for x in words:
    for i in range(1, len(x)):
        cur = x[i]
        prev = x[i - 1]
        tree[




# print(words)
