""""""
"""
The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:

The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. 
The daily cost of operating A is 160+40X^2.
The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. 
The daily cost of operating B is 128+40Y^2.
Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they 
operate like new at the start of each day. Find and print the expected daily cost for each machine.
"""

a, b = 0.88, 1.55

"""
E[X^2] = Var(X) + E[X]**2
"""
var1, var2 = 160, 128

"""
E[Ca] = 160 + 40[Var(X) + E[X]**2]
"""
ans1 = var1 + 40*(a + (a**2))
ans2 = var2 + 40*(b + (b**2))

print('%0.3f'%ans1)
print('%0.3f'%ans2)



