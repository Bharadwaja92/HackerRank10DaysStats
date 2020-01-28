""""""
"""
The final grades for a Physics exam taken by a large group of students have a mean of 70 and a standard deviation of 10.
If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

 * Scored higher than 80 (i.e., have a grade > 80)?
 * Passed the test (i.e., have a grade >= 60)?
 * Failed the test (i.e., have a grade < 80)?
"""
import math


def normal_distribution(x, mean, sd):
    nr = (x - mean)
    dr = sd * (2 ** 0.5)
    ans = 0.5 * (1 + math.erf(nr / dr))
    return ans*100


mean = 70
sd = 10
ans1 = 100 - normal_distribution(x=80, mean=mean, sd=sd)
ans2 = 100 - normal_distribution(x=60, mean=mean, sd=sd)
ans3 = normal_distribution(x=60, mean=mean, sd=sd)

print('%.2f' % ans1)
print('%.2f' % ans2)
print('%.2f' % ans3)



