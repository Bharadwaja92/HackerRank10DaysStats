""""""
"""
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because 
they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

No more than 2 rejects?
At least 2 rejects?
"""

import math


def calculate_combinations(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)


prob_reject = 0.12
num_pistons = 10

# 1. No more than 2 rejects - 0, 1, 2
ans1 = 0
for i in range(3):
    ans1 += calculate_combinations(num_pistons, i) * (prob_reject**i) * ((1-prob_reject)**(num_pistons-i))

print('%.3f'%ans1)
# 2. Atleast 2 rejects --> Not 0, 1
ans2 = 0
for i in range(2):
    ans2 += calculate_combinations(num_pistons, i) * (prob_reject**i) * ((1-prob_reject)**(num_pistons-i))

print('%.3f'%(1-ans2))

