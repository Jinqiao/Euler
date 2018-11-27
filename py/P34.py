import utils
import math

def p34():
    r = 0
    for n in range(3, 99999):
        s = 0
        for d in utils.getDigitsR(n):
            s += math.factorial(d)
        if s == n:
            print(s)
            r += s
    return r


p34()
