from utils import *


def getP27Func(a, b):
    def f(n):
        return n * n + a * n + b
    return f


def numOfPrimes(a, b):
    n = 0
    f = getP27Func(a, b)
    while isPrime(f(n)):
        n = n + 1
    return n


def solveP27():
    m = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = numOfPrimes(a, b)
            # if n > 39:
            #     print(f"n: {n}, a: {a}, b: {b}")
            if n > m:
                m = n
                print(f"max: {m}, a: {a}, b: {b}")


solveP27()
