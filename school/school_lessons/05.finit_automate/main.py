import numpy as np
fin = open('words.txt')

words_list = fin.readlines()
words_list = list(map(str.strip, words_list))
words_list = list(filter(lambda x: len(x) >= 4, words_list))

fin.close()


# print(*words_list, sep='\n')

SIZE = 127

def main(words):
    arr = np.zeros((SIZE, SIZE))

    for w in words:
        print(w)
        chars_ascii = list(map(ord, f' {w} '))

        # print(chars_ascii)

        for i in range(1, len(chars_ascii)):
            prev = chars_ascii[i - 1]
            cur = chars_ascii[i]
            # print(prev, cur)
            arr[prev, cur] += 1


    return arr

arr = main(words_list[:])

# print(arr[97])
for i in arr:
    print(i)

