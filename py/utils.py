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
