# Given an unsorted integer array, print all greater elements than all elements present to their right.
#
# Input : [10, 4, 6, 3, 5]
# Output: [10, 6, 5]
# Explanation: The elements that are greater than all elements to their right are 10, 6, and 5.
def greater_elements_to_right(arr):
    if not arr:
        return []
    result = []
    max_val = arr[-1]
    i = len(arr) - 2
    while i >= 0:
        if arr[i] > max_val:
            result.append(arr[i])
            max_val = arr[i]
        i -= 1
        if arr[-1] >= max_val:
            result.append(arr[-1])
    return result[::-1]


arr = [10, 4, 6, 3, 5]
print(greater_elements_to_right(arr))
