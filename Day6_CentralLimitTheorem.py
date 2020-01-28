""""""
"""
A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported 
via the elevator. The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a 
standard deviation of 15 pounds. Based on this information, what is the probability that all 49 boxes can be safely 
loaded into the freight elevator and transported?
"""
import math


def normal_distribution(x, mean, sd):
    nr = (x - mean)
    dr = sd * (2 ** 0.5)
    ans = 0.5 * (1 + math.erf(nr / dr))
    return ans


num_boxes = 49
mean, sd = 205, 15
new_mean = mean * num_boxes
new_sd = sd * (num_boxes**0.5)

print('new_mean =', new_mean)
print('new_sd =', new_sd)

ans = normal_distribution(x=9800, mean=new_mean, sd=new_sd)

print('%.4f' % ans)

