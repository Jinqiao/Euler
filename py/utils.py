import math

__jq_primes = set()


def isPrime(n):
    if n in __jq_primes:
        return True
    n = abs(n)
    if n in [0, 1, 2, 3]:
        return True
    i = 2
    ceil = math.sqrt(n)
    while (i <= ceil):
        if (n % i == 0):
            return False
        i = i + 1
    __jq_primes.add(n)
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


# def getGcd(a, b):
#     a_factors = getFactors(a)
#     b_factors = getFactors(b)
#     gcd = 1
#     for i in a_factors:
#         if i in b_factors:
#             gcd = gcd * i
#             b_factors.remove(i)
#     return gcd


# faster
def getGcd(a, b):
    if b == 0:
        return a
    else:
        return getGcd(b, a % b)


def isPandigital(n):
    m = str(n)
    s = set(m)
    if "0" in s:
        return False
    return (len(s) == len(m) and int(max(s)) == len(s))


def nextPrime(n):
    n = n + 1
    if n % 2 == 0:
        n = n + 1
    while (n % 3 == 0 or n % 5 == 0 or not isPrime(n)):
        n = n + 2
    return n


# def numberOfDigits(i):
#     n = 1
#     if i >= 100000000:
#         n = n + 8
#         i = i // 100000000
#     if i >= 10000:
#         n = n + 4
#         i = i // 10000
#     if i >= 100:
#         n = n + 2
#         i = i // 100
#     if i >= 10:
#         n = n + 1
#     return n

def numberOfDigits(i):
    return len(str(i))
