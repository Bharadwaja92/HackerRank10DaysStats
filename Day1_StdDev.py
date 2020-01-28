""""""
"""
Given an array, X, of N integers, calculate and print the standard deviation. Your answer should be in decimal form, 
rounded to a scale of 1 decimal place (i.e., 12.3 format). An error margin of +-0.1 will be tolerated for the SD.
"""

n = int(input())
nums = list(map(int, input().split()))

mean = sum(nums) / n

squared_deviations = [(x-mean)**2 for x in nums]

variance = sum(squared_deviations) / n

stddev = variance ** 0.5

print('%.1f'%stddev)

