# Find all elements in an array that are greater than all elements to their right
# Given an unsorted integer array, print all greater elements than all elements present to their right.
# For example, consider the array [10, 4, 6, 3, 5]. The elements that are greater than all elements to their
# right are 10, 6, and 5.
def find_elements(input_arr):
    result = []
    n = len(input_arr)
    for i in range(n):
        find_grt = True
        for j in range(i + 1, n):
            if input_arr[j] > input_arr[i]:
                find_grt = False
                break
        if find_grt:
            result.append(input_arr[i])
    return result


arr = [10, 4, 6, 3, 5]
print(find_elements(arr))
