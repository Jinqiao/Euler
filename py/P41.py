from utils import isPandigital, isPrime
from itertools import permutations
from math import pow


def getN(l):
    n = 0
    i = 0
    for k in l:
        n = n + k * pow(10, i)
        i = i + 1
    return int(n)


def Go():
    nums = list()
    for k in xrange(9, 5, -1):
        for l in permutations(range(1, k)):
            i = getN(l)
            if i % 5 == 0 or i % 3 == 0 or i % 7 == 0:
                continue
            if isPandigital(i) and isPrime(i):
                nums.append(i)
    print(max(nums))


Go()

# j = 0
# for i in xrange(98765431, 1, -2):
#     j = j + 1
#     if i % 5 == 0 or i % 3 == 0 or i % 7 == 0:
#         continue
#     if j % 1000000 == 0:
#         print(i)
#     if isPandigital(i) and isPrime(i):
#         print(i)
#         break
