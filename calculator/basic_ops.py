
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
    if 0 in args:
        print("cannot divide by zero.")
    for i in args:
        total = args[0]
        total /= i
    return total