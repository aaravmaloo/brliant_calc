import numpy as np
import math


def nth(*args):
    if len(args) != 2:
        return "the nth function requires exactly two arguments (number, n)."
    
    number, n = args
    if n == 0:
        return "n cannot be zero."

    return np.power(number, 1 / n)

def exp(*args):
    if len(args) != 1:
        return "the exp function requires exactly one argument."
    
    return np.exp(args[0])

def pow(*args):
    if len(args) != 2:
        return "the pow function requires exactly two arguments (base, exponent)."
    
    base, exponent = args
    return np.power(base, exponent)

def log(*args):
    if len(args) != 1:
        return "the log function requires exactly one argument."
    
    value = args[0]
    if value <= 0:
        return "logarithm is undefined for non-positive values."
    
    return np.log(value)

def log10(*args):
    if len(args) != 1:
        return "the log10 function requires exactly one argument."
    
    value = args[0]
    if value <= 0:
        return "logarithm is undefined for non-positive values."
    
    return np.log10(value)