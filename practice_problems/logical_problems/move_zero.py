# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Example 1:
# Input: nums = [0,1,0,3,12] Output: [1,3,12,0,0]
def move_zero(nums):
    zero_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
        else:
            nums[i - zero_count] = nums[i]
            nums[i] = 0
    return nums


nums = [0, 1, 0, 3, 5]
print(move_zero(nums))
