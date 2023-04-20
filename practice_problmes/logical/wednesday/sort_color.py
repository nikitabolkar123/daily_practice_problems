# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
# are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
# Given an array containing only 0’s, 1’s, and 2’s, in-place sort it in linear time and using constant space.
# Input : [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]

def sort_color(nums):
    for i in range(1, len(nums)):
        c_ele = nums[i]
        position = i
        while c_ele < nums[position - 1] and position > 0:
            nums[position] = nums[position - 1]
            position = position - 1
        nums[position] = c_ele
    return nums


if __name__ == '__main__':
    print(sort_color([2, 0, 2, 1, 1, 0]))
