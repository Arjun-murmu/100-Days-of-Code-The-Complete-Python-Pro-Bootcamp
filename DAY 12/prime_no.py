# ✅ 1. Naive Method (checks all numbers before num)
def is_prime_naive(num):
    if num <= 1:
        return False
    for i in range(2, num):  # check from 2 to num-1
        if num % i == 0:
            return False
    return True
  
# Time Complexity: O(n)

# ✅ 2. Optimized: Check up to √num (the standard method)
def is_prime_sqrt(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
# Time Complexity: O(√n)

# ✅ 3. Use Python's sympy Library
from sympy import isprime
print(isprime(29))  # True
