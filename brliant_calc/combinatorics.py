import math


def permutation(n, k):
    n, k = int(n), int(k)
    if n < 0 or k < 0:
        return "Error: n and k must be non-negative."
    if k > n:
        return 0
    return math.perm(n, k)

def combination(n, k):
    n, k = int(n), int(k)
    if n < 0 or k < 0:
        return "Error: n and k must be non-negative."
    if k > n:
        return 0
    return math.comb(n, k)

def multiset_combination(n, k):
    n, k = int(n), int(k)
    if n < 0 or k < 0:
        return "Error: n and k must be non-negative."
    return math.comb(n + k - 1, k)

def derangement(n):
    n = int(n)
    if n < 0:
        return "Error: Derangement not defined for negative integers."
    if n == 0:
        return 1
    if n == 1:
        return 0
    a, b = 1, 0
    for i in range(2, n + 1):
        a, b = b, (i - 1) * (a + b)
    return b

def stirling_second_kind(n, k):
    n, k = int(n), int(k)
    if n < 0 or k < 0:
        return "Error: Stirling numbers require non-negative integers."
    if k > n:
        return 0
    if k == 0:
        return 1 if n == 0 else 0
    if k == 1 or k == n:
        return 1
    result = 0
    for i in range(k + 1):
        sign = (-1) ** (k - i)
        result += sign * math.comb(k, i) * (i ** n)
    return result // math.factorial(k)

def bell_number(n):
    n = int(n)
    if n < 0:
        return "Error: Bell number not defined for negative integers."
    total = 0
    for k in range(n + 1):
        total += stirling_second_kind(n, k)
    return total

def partition_count(n):
    n = int(n)
    if n < 0:
        return "Error: Partition count not defined for negative integers."
    partitions = [0] * (n + 1)
    partitions[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]
    return partitions[n]

def stars_and_bars(n, k):
    n, k = int(n), int(k)
    if n < 0 or k <= 0:
        return "Error: n must be non-negative and k must be positive."
    return math.comb(n + k - 1, k - 1)

def catalan_number(n):
    n = int(n)
    if n < 0:
        return "Error: Catalan number not defined for negative integers."
    return math.comb(2 * n, n) // (n + 1)

def lah_number(n, k):
    n, k = int(n), int(k)
    if n < 0 or k < 0 or k > n:
        return 0
    if k == 0:
        return 0
    return math.comb(n - 1, k - 1) * math.factorial(n) // math.factorial(k)
