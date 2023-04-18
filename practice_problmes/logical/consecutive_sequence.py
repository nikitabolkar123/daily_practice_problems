# "Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence
# is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
# Examples
# consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True
# consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False
# consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False
# consecutive_combo([44, 46], [45]) ➞ True"
def consecutive_sequence(lst1, lst2):
    lst = lst1 + lst2
    lst.sort()
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1] + 1:
            return False
    return True


print(consecutive_sequence([7, 4, 5, 1], [2, 3, 6]))
print(consecutive_sequence([1, 4, 6, 5], [2, 7, 8, 9]))
