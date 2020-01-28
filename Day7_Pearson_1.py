
def get_mean_stdev(nums):
    mean = sum(nums) / n
    squared_deviations = [(x - mean) ** 2 for x in nums]
    variance = sum(squared_deviations) / n
    stddev = variance ** 0.5
    return mean, stddev


n = int(input())
nums1 = list(map(float, input(' ').split()))
nums2 = list(map(float, input(' ').split()))

m1, v1 = get_mean_stdev(nums1)
m2, v2 = get_mean_stdev(nums2)

print(m1, v1)
print(m2, v2)

numr = sum([(nums1[i]-m1)*(nums2[i]-m2) for i in range(n)])
denr = n * v1 * v2

print('%.3f' % (numr/denr))

