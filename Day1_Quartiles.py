""""""
"""
Given an array, X, of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and 
third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.
"""

# n = int(input())
# nums = list(map(int, input().split()))
# nums = sorted(nums)


def calc_median_uh_lh(n, nums):
    if n % 2 == 0:
        median = (nums[n//2] + nums[n//2 - 1]) / 2
        lh, uh = nums[: n//2], nums[n//2:]
    else:
        median_index = n // 2
        print('Median index =', median_index)
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


ip = '3 7 8 5 12 14 21 13 18'.split()
nums = list(map(int, ip))
nums = sorted(nums)
median, lh, uh = calc_median_uh_lh(len(nums), nums)
q1, q3 = get_q1_q3(lh), get_q1_q3(uh)
print(nums, lh, uh, median, q1, q3)

nums = sorted([6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49])
median, lh, uh = calc_median_uh_lh(len(nums), nums)
q1, q3 = get_q1_q3(lh), get_q1_q3(uh)
print(nums, lh, uh, median, q1, q3)

# nums = sorted([6, 7, 15, 36, 39, 40, 41, 42, 43, 47])
# median, lh, uh = calc_median_uh_lh(n, nums)
# q1, q3 = get_q1_q3(lh), get_q1_q3(uh)
# print(nums, lh, uh, median, q1, q3)
