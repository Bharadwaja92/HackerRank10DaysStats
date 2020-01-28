""""""
"""
A group of five students enrolls in Statistics immediately after taking a Math aptitude test. Each student's Math 
aptitude test score, x, and Statistics course grade, y, can be expressed as the following list of  points:

If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics? Determine 
the equation of the best-fit line using the least squares method, then compute and print the value of y when x = 80.
"""
x, y = [], []

n = 5
for i in range(n):
    n1, n2 = list(map(int, input().split()))
    x.append(n1)
    y.append(n2)

sum_x, sum_y = sum(x), sum(y)
mean_x, mean_y = sum_x/n, sum_y/n

sum_x_sq = sum([v*v for v in x])
sum_xy = sum([x[i]*y[i] for i in range(n)])

b_nr = (n*sum_xy) - (sum_x*sum_y)
b_dr = (n*sum_x_sq) - (sum_x*sum_x)

b = b_nr / b_dr

a = mean_y - (b*mean_x)

print('a =', a, 'b =', b)
ans = a + (b*80)
print('ans =', ans)

from sklearn.linear_model import LinearRegression
import numpy as np
x = np.asarray(x).reshape(-1, 1)

lm = LinearRegression()
lm.fit(x, y)

a = lm.intercept_
b = lm.coef_[0]
print('a =', a, 'b =', b)
ans = a + (b*80)
print('ans =', ans)



