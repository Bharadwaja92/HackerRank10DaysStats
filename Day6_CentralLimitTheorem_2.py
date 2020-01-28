""""""
"""
The number of tickets purchased by each student for the University X vs. University Y football game follows a 
distribution that has a mean of 2.4 and a standard deviation of 2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 
tickets left, what is the probability that all 100 students will be able to purchase tickets?
"""

import math


def normal_distribution(x, mean, sd):
    nr = (x - mean)
    dr = sd * (2 ** 0.5)
    ans = 0.5 * (1 + math.erf(nr / dr))
    return ans


mean = 2.4
sd = 2.0
num_students = 100
new_mean = mean * num_students
new_sd = sd * (num_students**0.5)

ans = normal_distribution(x=250, mean=new_mean, sd=new_sd)
print('%.4f' % ans)
