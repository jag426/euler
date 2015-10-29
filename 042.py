from util import is_triangle

def value(word):
    return sum(map(lambda c: ord(c) - ord('A') + 1, word))

words = open('p042_words.txt').read().strip('"').split('","')
print(len(list(filter(is_triangle, map(value, words)))))
