# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
# element is distinct.
# Input: nums = [1,2,3,1]
# Output: true
def contains_duplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


nums = [1, 2, 3, 1]
print(contains_duplicate(nums))


def contains_duplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


nums = [1, 2, 3, 4]
print(contains_duplicate(nums))
