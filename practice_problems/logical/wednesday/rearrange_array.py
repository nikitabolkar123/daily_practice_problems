# Rearrange an array with alternate high and low elements
# Given an integer array, rearrange it such that every second element becomes greater than its left and right elements.
# Assume no duplicate elements are present in the array.

# example,
#
# Input: {1, 2, 3, 4, 5, 6, 7}
# Output: {1, 3, 2, 5, 4, 7, 6}
#
# Input: {9, 6, 8, 3, 7}
# Output: {6, 9, 3, 8, 7}
#
# Input: {6, 9, 2, 5, 1, 4}
# Output: {6, 9, 2, 5, 1, 4}
def rearrange_array(nums):
    n = len(nums)
    for i in range(1, n, 2):
        if i > 0 and nums[i] < nums[i - 1]:
            temp = nums[i]
            nums[i] = nums[i - 1]
            nums[i - 1] = temp
        if i < n - 1 and nums[i] < nums[i + 1]:
            temp = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = temp
    return nums


nums1 = [1, 2, 3, 4, 5, 6, 7]
nums2 = [9, 6, 8, 3, 7]

# print(rearrange_array(nums1))
# print(rearrange_array(nums2))

for i in range(15, -1,-2):
    print(i)