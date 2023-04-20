# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist
# , return the maximum number.
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
def third_max(nums):
    nums = sorted(list(nums))
    return nums[-3] if len(nums) >= 3 else nums[-1]


nums = [3,4,2, 1,8,6]
print(third_max(nums))
