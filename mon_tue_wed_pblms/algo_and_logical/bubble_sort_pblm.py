# 30. Write a Python program to sort unsorted numbers using Recursive Bubble Sort. Go to the editor
def recursive_bubble_sort(arr, n):
    if n == 1:
        return arr

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp

    return recursive_bubble_sort(arr, n - 1)


arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
sorted_arr = recursive_bubble_sort(arr, n)
print("Sorted array:", sorted_arr)
