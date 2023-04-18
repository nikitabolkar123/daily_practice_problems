# Find the duplicate element in a limited range array
# Google Translate Icon
# Given a limited range array of size n containing elements between 1 and n-1 with one element repeating,
# find the duplicate number in it without using any extra space.
# For example,
#
# Input: {1, 2, 3, 4, 4}
# Output: The duplicate element is 4
#
# Input: {1, 2, 3, 4, 2}
# Output: The duplicate element is 2
def find_duplicate(arr):
    n = len(arr)
    for i in range(n):
        # access index
        index = arr[i] - 1  # If the element at the index is positive, negate it
        if arr[index] > 0:
            arr[index] = -arr[index]
        else:  # duplicate ele
            return index + 1


arr1 = [1, 2, 3, 4, 4]
print(find_duplicate(arr1))

arr2 = [1, 2, 3, 4, 2]
print(find_duplicate(arr2))
