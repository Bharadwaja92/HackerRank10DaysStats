""""""
"""
The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of 
Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 
decimal places (i.e., 1.234 format).
"""
from scipy.special import comb

# b, g = list(map(int, input().split()))
b, g = 1.09, 1

b, g = b/(b+g), g/(b+g)

n = 6
p = 3

# Atleast 3 boys
ans = 0
for i in range(3, 7):
    ans += comb(6, i) * (b**i) * (g**(6-i))

# ans = (comb(6, 3)*(b**3)*(g**3)) + (comb(6, 4)*(b**4)*(g**2)) + (comb(6, 5)*(b**5)*(g**1)) + (comb(6, 6)*(b**6)*(g**0))
# 57.983

print('%.3f'%ans)

