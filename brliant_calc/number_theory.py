import math
from functools import lru_cache


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 2:
        factors.append(n)
    return factors

def gcd(*args):
    result = 0
    for a in args:
        result = math.gcd(result, int(a))
    return result

def lcm(*args):
    if not args:
        return 0
    result = int(args[0])
    for a in args[1:]:
        a = int(a)
        result = result * a // math.gcd(result, a)
    return result

@lru_cache(maxsize=128)
def fibonacci(n):
    n = int(n)
    if n < 0:
        return "Error: Fibonacci not defined for negative numbers."
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def nth_prime(n):
    n = int(n)
    if n < 1:
        return "Error: n must be a positive integer."
    count = 0
    candidate = 2
    while True:
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate
        candidate += 1

def euler_totient(n):
    n = int(n)
    if n < 1:
        return "Error: Euler's totient is defined for positive integers."
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result

def catalan(n):
    n = int(n)
    if n < 0:
        return "Error: Catalan number not defined for negative integers."
    return math.comb(2 * n, n) // (n + 1)

def binomial(n, k):
    n, k = int(n), int(k)
    if n < 0 or k < 0:
        return "Error: Binomial coefficient requires non-negative integers."
    return math.comb(n, k)

def mod_inverse(a, m):
    a, m = int(a), int(m)
    if m <= 0:
        return "Error: Modulus must be positive."
    g, x, _ = _extended_gcd(a % m, m)
    if g != 1:
        return "Error: Modular inverse does not exist (numbers not coprime)."
    return x % m

def _extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = _extended_gcd(b % a, a)
    return g, y - (b // a) * x, x

def prime_sieve(n):
    n = int(n)
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]

def digit_sum(n):
    n = abs(int(n))
    return sum(int(d) for d in str(n))

def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(int(n)))[::-1])

def is_palindrome(n):
    s = str(abs(int(n)))
    return s == s[::-1]

def collatz_steps(n):
    n = int(n)
    if n <= 0:
        return "Error: Collatz sequence requires positive integer."
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def perfect_number_check(n):
    n = int(n)
    if n < 2:
        return False
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n

def goldbach_partitions(n):
    n = int(n)
    if n <= 2 or n % 2 != 0:
        return []
    partitions = []
    for p in range(2, n // 2 + 1):
        if is_prime(p) and is_prime(n - p):
            partitions.append((p, n - p))
    return partitions
