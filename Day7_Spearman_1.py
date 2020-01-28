def get_mean_stdev(nums):
    mean = sum(nums) / n
    squared_deviations = [(x - mean) ** 2 for x in nums]
    variance = sum(squared_deviations) / n
    stddev = variance ** 0.5
    return mean, stddev


def get_ranks(nums):
    srted = sorted(nums)
    ranked = []
    for i in range(len(nums)):
        ranked.append(srted.index(nums[i]) + 1)
    return ranked


n = int(input())
nums1 = list(map(float, input(' ').split()))
nums2 = list(map(float, input(' ').split()))

ranked1 = get_ranks(nums1)
ranked2 = get_ranks(nums2)

# print(ranked1)
# print(ranked2)

dsq = [(ranked1[i] - ranked2[i])**2 for i in range(n)]

nr = 6 * sum(dsq)
dr = n * (n*n - 1)

print('%.3f' % (1 - (nr/dr)))

# m1, v1 = get_mean_stdev(nums1)
# m2, v2 = get_mean_stdev(nums2)


