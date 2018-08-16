from utils import getFactors
from operator import mul


def isPandigitalProd(n):
    s = split(n)
    for pair in s:
        digitsStr = str(n)
        for d in pair:
            digitsStr = digitsStr + str(d)
        if len(digitsStr) != 9 or '0' in digitsStr:
            continue
        if len(set(digitsStr)) == 9:
            return True
    return False


def getSubsets(s):
    n = len(s)
    r = set()
    for i in xrange(1, 1 << n):
        subsetElem = []
        for j in xrange(0, n):
            if i & (1 << j):
                subsetElem.append(s[j])
        r.add(tuple(subsetElem))
    return r


def split(n):
    subsets = getSubsets(getFactors(n))
    n1s = set()
    r = set()
    for s in subsets:
        n1s.add(reduce(mul, s))
    for n1 in n1s:
        n2 = n / n1
        r.add((min(n1, n2), max(n1, n2)))
    return r


def calculate():
    t = 0
    for i in xrange(1002, 9999):
        if isPandigitalProd(i):
            t = t + i
    print(t)


calculate()
