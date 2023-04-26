# Given a list and a set, return a sorted list with its items in ascending order but prioritize the elements in the
# set over the other items in the list.
#
# Examples
# priority_sort([5, 4, 3, 2, 1], {2, 3}) ➞ [2, 3, 1, 4, 5]
#
# priority_sort([5, 4, 3, 2, 1], {3, 6}) ➞ [3, 1, 2, 4, 5]
#
# priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}) ➞ [-4, -3, -5, -2, -1, 0]
# Notes
# If the list is empty, return an empty list.
# If the set is empty there is nothing to prioritize, but the list should still be sorted.
# The set may contain values that are not in the list.
# The list may contain duplicates.
# The list and the set will only contain integer values
def priority_sort(lst, set1):
    res = []
    for i in range(len(lst)):
        if lst[i] in set1:          # here we check if the item at the current index is in the set
            # If the item is in the set, add it to the result
            res.append(lst[i])
        else:
            pass
    # Sort the remaining items in the list and add them to the result
    remaining_items = sorted(set(lst) - set(set1))
    res += remaining_items
    return res


print(priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}))
