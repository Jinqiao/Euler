import utils as ut
from utils import nextPrime
from utils import numberOfDigits
from utils import isPrime
from itertools import combinations

primes = [3, 5, 7]  # 2 is not possible
pairCache = dict()
twoPairCache = dict()
all_primes = None


def getNextPrime():
    p = nextPrime(primes[-1])
    primes.append(p)
    return p


def isPairOk(a, b):
    if (a, b) in pairCache:
        return pairCache[(a, b)]
    # n1 = a * 10**numberOfDigits(b) + b
    # n2 = b * 10**numberOfDigits(a) + a
    n1 = int(str(a) + str(b))
    n2 = int(str(b) + str(a))

    # the bottle neck is the isPrime() function below if somehow we
    # can have a upper limit we can generate all the primes up to that
    # limit up front
    # ok1 = isPrime(n1) and isPrime(n2)

    global all_primes
    if all_primes is None:
        print("Init primes")
        all_primes = set(ut.primes_sieve(100000000))
    ok = (n1 in all_primes) and (n2 in all_primes)
    pairCache[(a, b)] = ok
    return ok


def are2PairsOk(pair1, pair2):
    if (pair1, pair2) in twoPairCache:
        return twoPairCache[(pair1, pair2)]
    a, b = pair1[0], pair1[1]
    c, d = pair2[0], pair2[1]
    ok = isPairOk(a, c) and isPairOk(a, d) and isPairOk(b, c) and isPairOk(b, d)
    twoPairCache[(pair1, pair2)] = ok
    return ok


def isNextPrimeOk():
    newP = getNextPrime()
    oldPrimesCanPairWithNewP = []
    for oldP in primes[:-1]:
        if isPairOk(oldP, newP):
            oldPrimesCanPairWithNewP.append(oldP)
    pairs = [(a, b) for (a, b) in combinations(oldPrimesCanPairWithNewP, 2)
             if isPairOk(a, b)]
    if len(pairs) > 0:
        pairOfPairs = [(pair1, pair2) for (pair1, pair2) in combinations(pairs, 2)
                       if are2PairsOk(pair1, pair2)]
        if len(pairOfPairs) > 0:
            print(pairOfPairs)
            print(pairOfPairs[0])
            print(sum(sum(pairOfPairs[0], ()), primes[-1]))
            return True
    return False


def go():
    global primes
    primes = [3, 5, 7]
    while not isNextPrimeOk():
        length = len(primes)
        if length % 20 == 0:
            print(f'length = {length}, p = {primes[-1]}')


# Below works, but too slow..
# def canAddToTupple(tup, b):
#     for a in tup:
#         if not isPairOk(a, b):
#             return False
#     return True

# def getNextSetOfTuples(ts):
#     s = set()
#     for tup in ts:
#         for p in primes:
#             if p not in tup and canAddToTupple(tup, p):
#                 s.add((*tup, p))
#     return s

# while 1979 not in primes:
#     getNextPrime()

# pairs = [(a, b) for a, b in combinations(primes, 2) if isPairOk(a, b)]
# s3 = getNextSetOfTuples(pairs)
# s4 = getNextSetOfTuples(s3)
# s5 = getNextSetOfTuples(s4)

# def updatePairs():
#     updated = False
#     p = getNextPrime()
#     for p0 in primes[:-1]:
#         if isPairOk(p0, p):
#             pairs.append((p0, p))
#             updated = True
#     return updated

# def updateTupleSet(ts1, ts2):
#     p = primes[-1]
#     for tup in ts1:
#         if p not in tup and canAddToTupple(tup, p):
#             ts2.add((*tup, p))

# while True:
#     if updatePairs():
#         updateTupleSet(pairs, s3)
#         updateTupleSet(s3, s4)
#         updateTupleSet(s4, s5)
#         if len(s5) > 0:
#             print(s5)
#             break

# t = []
# for x in s5:
#     t.append(x)
# print(sum(t[0]))
