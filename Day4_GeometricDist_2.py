""""""
"""
The probability that a machine produces a defective product is 1/3. 
What is the probability that the 1st defect is found during the 5th inspection?
"""

nr, dr = list(map(int, input().split()))
p = nr/dr
q = 1-p
n = int(input())

ans = 0

for i in range(1, 6):
    ans += (q**(i-1)) * p


print('%.3f'%(ans))

