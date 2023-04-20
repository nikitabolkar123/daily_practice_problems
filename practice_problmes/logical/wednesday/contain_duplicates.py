# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
# that nums[i] == nums[j] and abs(i - j) <= k.
# Example
# 1:
#
# Input: nums = [1, 2, 3, 1], k = 3
# Output: true
# Example
# 2:
#
# Input: nums = [1, 0, 1, 1], k = 1 ##nums[0] = nums[2] = 1, |0 - 2| = 2,, which is less than or equal to k = 1. true.
# Output: true
# Example
# 3
# Input: nums = [1, 2, 3, 1, 2, 3], k = 2 ...no disinct elemnts
# Output: false
def contains_duplicate(nums, k):
    if len(nums) < 2:
        return False
    num_indexes = {}
    for i in range(len(nums)):
        num = nums[i]
        if num in num_indexes and i - num_indexes[num] <= k:
            return True
        else:
            num_indexes[num] = i
    return False


nums = [1, 2, 3, 1]  # (0-3)=3 here nums[0] = nums[3] = 1 which is less than or equal to k = 3....returns true.
k = 3
print(contains_duplicate(nums, k))
