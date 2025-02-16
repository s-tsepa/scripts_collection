import random

a = 4
b = 4

fin = open('words.txt')

w = list(map(str.strip, fin.readlines()))
w = list(filter(lambda x: a <= len(x) <= b, w))

random.shuffle(w)

print(*w, sep='\n')
