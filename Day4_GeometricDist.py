""""""
"""
The probability that a machine produces a defective product is 1/3. 
What is the probability that the 1st defect is found during the 5th inspection?
"""

p = 1/3

ans = ((1-p)**4) * p

print('%.3f'%(ans))


