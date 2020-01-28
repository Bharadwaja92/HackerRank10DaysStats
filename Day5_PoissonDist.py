""""""
"""
A random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with which the 
random variable X is equal to 5.
"""
import math


def calculate_combinations(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)


l = float(input())
k = int(input())

e = math.e
"""
P(k, l) = (l^k) * (e^-l) / fact(k)
"""

ans = (l**k) * (e**-l) / math.factorial(k)

print('%.3f'%ans)




