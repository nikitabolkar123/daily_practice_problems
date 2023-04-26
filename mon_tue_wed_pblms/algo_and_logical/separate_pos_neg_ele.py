# Segregate positive and negative integers using merge sort
# Google Translate Icon
# Given an array of positive and negative integers, segregate them without changing the relative order of elements. The
# output should contain all positive numbers follow negative numbers while maintaining the same relative ordering.
# For example,
#
# Input:  [9, -3, 5, -2, -8, -6, 1, 3]
# Output: [-3, -2, -8, -6, 9, 5, 1, 3]
def segregate_numbers(arr):
    def merge(arr, left, mid, right):
        i = left
        j = mid + 1
        aux = []
        while i <= mid and j <= right:
            if arr[i] < 0 and arr[j] < 0:
                if arr[i] <= arr[j]:
                    aux.append(arr[i])
                    i += 1
                else:
                    aux.append(arr[j])
                    j += 1
            elif arr[i] >= 0 and arr[j] >= 0:
                if arr[i] <= arr[j]:
                    aux.append(arr[i])
                    i += 1
                else:
                    aux.append(arr[j])
                    j += 1
            elif arr[i] < 0 and arr[j] >= 0:
                aux.append(arr[i])
                i += 1
            else:
                aux.append(arr[j])
                j += 1

        while i <= mid:
            aux.append(arr[i])
            i += 1

        while j <= right:
            aux.append(arr[j])
            j += 1

        for k in range(len(aux)):
            arr[left+k] = aux[k]

    def merge_sort(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid+1, right)
            merge(arr, left, mid, right)

    merge_sort(arr, 0, len(arr)-1)
    return arr


arr = [9, -3, 5, -2, -8, -6, 1, 3]
print(segregate_numbers(arr))
