""""""
"""
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3-Q1).
Given an array, X, of n integers and an array, F, representing the respective frequencies of X's elements, construct a 
data set, S, where each xi occurs at frequency fi. Then calculate and print 's interquartile range, rounded to a scale 
of 1 decimal place (i.e., 12.3 format).

Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number 
of elements, and be sure to not include the median in your upper and lower data sets.
"""

n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

nums = []
for i in range(n):
    nums.extend([l1[i]]*l2[i])

nums = sorted(nums)


def calc_median_uh_lh(n, nums):
    if n % 2 == 0:
        median = (nums[n//2] + nums[n//2 - 1]) / 2
        lh, uh = nums[: n//2], nums[n//2:]
    else:
        median_index = n // 2
        # print('Median index =', median_index)
        median = nums[median_index]
        lh, uh = nums[:median_index], nums[median_index+1: ]
    return median, lh, uh


def get_q1_q3(nums):
    n = len(nums)
    if n % 2 == 0:
        q = (nums[n // 2] + nums[n // 2 - 1]) / 2
    else:
        median_index = n // 2
        q = nums[median_index]
    return q


median, lh, uh = calc_median_uh_lh(len(nums), nums)
q1, q3 = get_q1_q3(lh), get_q1_q3(uh)
print(q1, q3)
print('%.1f'%(q3-q1))

"""
import statistics as st

n = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(n):
    s += [data[i]] * freq[i]
N = sum(freq)
s.sort()

if n%2 != 0:
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2+1:])
else:
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2:])

ir = round(float(q3-q1), 1)
print(ir)
"""