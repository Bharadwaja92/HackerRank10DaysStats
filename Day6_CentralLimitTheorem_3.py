""""""
"""
You have a sample of 100 values from a population with mean 500 and with standard deviation 80. Compute the interval 
that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that 
P(A < X < B) = 0.95. Use the value of z=1.96. Note that z is the z-score.
"""
import math


def normal_distribution(x, mean, sd):
    nr = (x - mean)
    dr = sd * (2 ** 0.5)
    ans = 0.5 * (1 + math.erf(nr / dr))
    return ans


num_samples, mean, sd = 100, 500, 80
z_score = 1.96
new_sd = sd / (num_samples**0.5)

margin_of_error = z_score * new_sd

lower_limit, upper_limit = mean - margin_of_error, mean + margin_of_error

print('%.2f' % lower_limit)
print('%.2f' % upper_limit)




