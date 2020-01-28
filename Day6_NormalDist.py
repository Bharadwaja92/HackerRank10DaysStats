""""""
"""
In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a 
mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled at this plant in:
 * Less than 19.5 hours?
 * Between 20 and 22 hours?
"""
import math


def normal_distribution(x, mean, sd):
    nr = (x - mean)
    dr = sd * (2 ** 0.5)
    ans = 0.5 * (1 + math.erf(nr / dr))
    return ans


e = math.e
pi = math.pi
ans1 = normal_distribution(x=19.5, mean=20, sd=2)

ans2 = normal_distribution(x=22, mean=20, sd=2) - normal_distribution(x=20, mean=20, sd=2)

print('%.3f'%ans1)
print('%.3f'%ans2)


a, b = 20, 22





