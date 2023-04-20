# Given an array of integers nums, calculate the pivot index of this array. The pivot index is the index where the
# sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the
# index's right. If the index is on the left edge of the array, then the left sum is 0 because there are no elements
# to the left. This also applies to the right edge of the array. Return the leftmost pivot index. If no such index
# exists, return -1.
# Example 1:
#
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
# Example 3:
#
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0
# the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.


def pivotIndex(nums):
    n = len(nums)
    if n == 0:
        return -1

    total_sum = sum(nums)

    # Initialize the left sum to 0
    left_sum = 0

    for i in range(n):
        # Calculate the right sum
        right_sum = total_sum - left_sum - nums[i]

        # Check if the left sum is equal to the right sum
        if left_sum == right_sum:
            return i

        left_sum += nums[i]  # Update the left sum

    return -1  # If no pivot index is found, return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))


# print(pivotIndex([2, 1, -1]))
#
# For i=0, left_sum=0, right_sum=7+3+6+5+6=27
# For i=1, left_sum=1, right_sum=3+6+5+6=20
# For i=2, left_sum=1+7=8, right_sum=6+5+6=17
# For i=3, left_sum=1+7+3=11, right_sum=5+6=11
def pivotIndex(nums):
    sum1 = sum(nums)
    p = 0
    for i, x in enumerate(nums):
        if p == sum1 - x - p:
            return i
        p += x
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
