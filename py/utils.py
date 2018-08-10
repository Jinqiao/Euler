import math


def isPrime(n):
    n = abs(n)
    if n in [0, 1, 2, 3]:
        return True
    i = 2
    ceil = math.sqrt(n)
    while(i <= ceil):
        if(n % i == 0):
            return False
        i = i + 1
    return True


def getFactors(n):
    n = o = abs(n)
    i = 2
    factors = []
    up_bound = math.sqrt(n)
    while i <= up_bound and n > 1:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i = i + 1
    if len(factors) == 0:
        factors.append(o)
        n = 1
    if n > 1:
        factors.append(n)
    return factors
