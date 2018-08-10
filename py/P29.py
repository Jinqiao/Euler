from utils import getFactors


def p29(ceil):
    s = set()
    ceil = ceil + 1
    for a in range(2, ceil):
        for b in range(2, ceil):
            # this is slow...
            # t = getPowerNumberFactors(a, b)

            # this is faster
            t = a**b
            s.add(t)
            # print(f"len(s): {len(s)}, a: {a}, b: {b}")
    return s


def getPowerNumberFactors(a, b):
    f = getFactors(a)
    f = f * b
    f.sort()
    return tuple(f)


print(len(p29(100)))
