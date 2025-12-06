import numpy as np
import math
from functools import lru_cache

def nth(number, n):
    if n == 0:
        return "n cannot be zero."
    return np.power(number, 1 / n)

def exp(x):
    return np.exp(x)

def pow(base, exponent):
    return np.power(base, exponent)

def log(value):
    if value <= 0:
        return "logarithm is undefined for non-positive values."
    return np.log(value)

def log10(value):
    if value <= 0:
        return "logarithm is undefined for non-positive values."
    return np.log10(value)

@lru_cache(maxsize=128)
def fact(n):
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    if not isinstance(n, int) or n < 0:
        return "factorial is only defined for non-negative integers."
    return math.factorial(n)



def convolve(signal, kernel):
    return np.convolve(signal, kernel, mode='full')
