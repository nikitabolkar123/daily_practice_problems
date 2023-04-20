# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing
# from the array.
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range
# since it does not appear in nums.
# Example 2:
#
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the
# range
# since it does not appear in nums.

def missing_number(nums):
    n = len(nums)
    expected_sum = (n * (n + 1)) / 2
    actual_sum = 0
    for num in nums:
        actual_sum += num
    return int(expected_sum - actual_sum)


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missing_number(nums))
