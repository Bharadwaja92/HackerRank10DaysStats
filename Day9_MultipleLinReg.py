""""""
"""
Andrea has a simple equation:
Y = a + b1.f1+ b2.f2 + ....bm.fm
for (m+1) real constants (a, f1, f2, ...fm). We can say that the value of Y depends on m features. Andrea studies this 
equation for n different feature sets (f1, f2, ...fm) and records each respective value of Y. If she has q new feature 
sets, can you help Andrea find the value of Y for each of the sets?
"""

from sklearn import linear_model

first = list(map(int, str.split(input(), " ")))
m, n = first[0], first[1]

data = [list(float(x) for x in input().split()) for i in range(n)]

x = [[item[i] for i in range(m)] for item in data]
y = [item[-1] for item in data]
lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_

for i in range(int(input())):
    data = list(map(float, input().split()))
    ans = [b[j] * data[j] for j in range(m)]
    print(a + sum(ans))



