from utils import nextPrime
from utils import numberOfDigits
from utils import isPrime
from itertools import combinations

primes = [3, 5, 7]  # 2 is not possible


def getNextPrime():
    p = nextPrime(primes[-1])
    primes.append(p)
    length = len(primes)
    if length % 20 == 0:
        print(f'length = {length}, p = {p}')
    return p


def isPairOk(a, b):
    n1 = a * 10 ** numberOfDigits(b) + b
    n2 = b * 10 ** numberOfDigits(a) + a
    return isPrime(n1) and isPrime(n2)


def isListOk(l):
    for a, b in l:
        if not isPairOk(a, b):
            return False
    return True


def canAddToTupple(tup, b):
    for a in tup:
        if not isPairOk(a, b):
            return False
    return True


def getNextSetOfTuples(ts):
    s = set()
    for tup in ts:
        for p in primes:
            if p not in tup and canAddToTupple(tup, p):
                s.add((*tup, p))
    return s


while 1979 not in primes:
    getNextPrime()

pairs = [(a, b) for a, b in combinations(primes, 2) if isPairOk(a, b)]
s3 = getNextSetOfTuples(pairs)
s4 = getNextSetOfTuples(s3)
s5 = getNextSetOfTuples(s4)


def updatePairs():
    updated = False
    p = getNextPrime()
    for p0 in primes[:-1]:
        if isPairOk(p0, p):
            pairs.append((p0, p))
            updated = True
    return updated


def updateTupleSet(ts1, ts2):
    p = primes[-1]
    for tup in ts1:
        if p not in tup and canAddToTupple(tup, p):
            ts2.add((*tup, p))


while True:
    if updatePairs():
        updateTupleSet(pairs, s3)
        updateTupleSet(s3, s4)
        updateTupleSet(s4, s5)
        if len(s5) > 0:
            print(s5)
            break

t = []
for x in s5:
    t.append(x)
print(sum(t[0]))
