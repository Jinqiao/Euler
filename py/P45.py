from math import sqrt


def isPent(c):
    x = (1 + sqrt(1 + 24 * c)) / 6.0
    return x == int(x)



def isHex(c):
    x = (1 + sqrt(1 + 8 * c)) / 4.0
    return x == int(x)


n = 285
while True:
    n = n + 1
    c = n * (n + 1) / 2
    if isPent(c) and isHex(c):
        break

print(c)
