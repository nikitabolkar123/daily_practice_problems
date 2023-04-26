# iven two lists smlst and biglst, we say smlst is an ordered sublist of biglst if all the elements of smlst can be
# found in biglst, and in the same order.
#
# Examples:
#
# [4, 3, 2] is an ordered sublist of [5, 4, 3, 2, 1]. [5, 3, 1] is an ordered sublist of [5, 4, 3, 2, 1]. [5, 3,
# 1] is not and ordered sublist of [1, 2, 3, 4, 5] since elements are not in the same - [1, 2, 3] is an ordered
# sublist of [3, 2, 1, 2, 3]. Write a function that, given lists smlst and biglst, decides if smlst is an ordered
# sublist of biglst.
#
# Examples
# is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]) ➞ True
#
# is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1]) ➞ True
#
# is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]) ➞ False
#
# is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]) ➞ True
# Notes
# Be careful of examples like the fourth example, where the elements of smlst appear multiple times in biglst.

def is_ord_sub(smllst, biglst):
    count = 0
    idx = 1
    for i in range(len(smllst)):
        for j in range(idx, len(biglst)):
            if smllst[i] == biglst[j]:
                idx = j
                count += 1
                if count == 3:
                    return True
    return False


print(is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]))
print(is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]))
print(is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]))
print(is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]))


def is_ord_sub(smllst, biglst):
    for i in range(len(smllst)):
        for j in range(0, len(biglst)):
            if smllst[i] == biglst[j]:
                pass

        # if i in biglst:
        #     if all(x in smllst for x in biglst):
        #         return False
    return True

# print(is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]))
