from math import sqrt


def isTriangleN(t):
    k = int(sqrt(2 * t))
    return k*(k+1) / 2 == t


def wordValue(w):
    n = 0
    for c in w:
        n = n + ord(c) - 64
    return n


def go():
    with open('p042_words.txt', 'r') as f:
        data = f.read()
    n = 0
    for w in data.split(','):
        v = wordValue(w.strip('"'))
        if isTriangleN(v):
            n = n + 1
    print("there are %d triangle words" % n)


go()
