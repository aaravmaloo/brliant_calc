import math


def add(*args):
    total = 0
    for i in args:
        total += i
    return total

def sub(*args):
    total = 0
    for i in args:
        total -= i
    return total

def mul(*args):
    total = 1
    for i in args:
        total *= i
    return total

def div(*args):
    if 0 in args[1:]:  
        return "cannot divide by zero."
    total = args[0]  
    for i in args[1:]: 
        total /= i
    return total

def mod(*args):
    if len(args) != 2:
        return "the mod function requires exactly two arguments (dividend, divisor)."
    
    dividend, divisor = args
    if divisor == 0:
        return "cannot divide by zero."
    
    return math.fmod(dividend, divisor)