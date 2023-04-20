# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at
# least two elements. You may return the answer in any order.
# Example 1:
#
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# Example 2:
#
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]

def find_subsequences(nums):
    result = []
    n = len(nums)

    def d(start, path):
        if len(path) >= 2:
            result.append(path[:])
        for i in range(start, n):
            if not path or nums[i] >= path[-1]:
                path.append(nums[i])
                d(i + 1, path)
                path.pop()

    d(0, [])
    return result


nums = [4, 6, 7, 7]
result = find_subsequences(nums)
print(result)
