fin = open('words.txt')
words = list(map(str.strip, fin.readlines()))

for w in words:
    if len(w) <= 4:
        print(w)
