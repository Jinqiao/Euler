from __future__ import division
from utils import getGcd


def isNonTrivialDigitCancel(a, b):
    if a < 10 or a > 99 or b < 10 or b > 99:
        raise ValueError('argument out of range')
    if a == b or a % 10 == 0 or b % 10 == 0:
        return False
    a1, a2 = a // 10, a % 10
    b1, b2 = b // 10, b % 10
    if a1 == a2 or b1 == b2:
        return False
    if a1 == b2 and a2 / b1 == a / b:
        return True
    if a2 == b1 and a1 / b2 == a / b:
        return True
    return False


def getP33Numbers():
    r = []
    for i in range(10, 100):
        for j in range(10, i):
            if isNonTrivialDigitCancel(j, i):
                r.append((j, i))
    return r


def solveP33():
    n, d = 1, 1
    for pair in getP33Numbers():
        d = d * pair[1]
        n = n * pair[0]
    print(d / getGcd(d, n))


solveP33()
