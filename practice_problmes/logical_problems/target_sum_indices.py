# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]


def two_sum(nums, target):
    num_indices = {}
    for i in range(len(nums)):
        num = nums[i]
        sum = target - num
        if sum in num_indices:
            return [num_indices[sum], i]
        num_indices[num] = i
    return []


nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))


def target(lst):
    lst1 = []
    target = 9
    for i in range(len(lst) - 1):
        for j in range(i, i + 1):
            if lst[i] + lst[i + 1] == target:
                lst1.append(i)
    return lst1


nums = [2, 7, 11, 15]
print(target(nums))
