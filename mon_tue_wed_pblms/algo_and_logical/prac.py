# def sum(minute):
#     return minute * 60
#
#
# print(sum(5))
#
#
# def area_of_tringle(hr):
#     sec = 60
#     return hr * sec * sec
#
#
# print(area_of_tringle(2))
#
#
# def range(flag):
#     return "True" if flag == True else False
#
#
# print(range(True))
#
#
# def str(l, b):
#     return (l + b) * 2
#
#
# print(str(10, 20))
#
#
# def calculate_exponent(num, exp):
#     return num ** exp
#
#
# def add(n1, n2):
#     a = [None, ""]
#     if n1 in a or n2 in a:
#         return "Invalid Operation"
#     return int(n1) + int(n2)
#
#
# print(add("80", "10"))


#
# Given a list of 10 numbers, return whether or not the list is shuffled sufficiently enough. In this case,
# if 3 or more numbers appear consecutively (ascending or descending), return False.
#
# Examples
# is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]) ➞ False
# # 1, 2, 3 appear consecutively
#
# is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]) ➞ False
# # 9, 8, 7, 6 appear consecutively
#
# is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]) ➞ True # No consecutive numbers appear is_shuffled_well([1, 3, 5,
# 7, 9, 2, 4, 6, 8, 10]) ➞ True # No consecutive numbers appear Notes Only steps of 1 in either direction count as
# consecutive (i.e. a sequence of odd and even numbers would count as being properly shuffled (see example #4)). You
# will get numbers from 1-10.
def is_shuffled_well(lst):
    count = 1
    prev_no = lst[0]
    for i in range(1, len(lst)):
        num = lst[i]
        if num == prev_no + 1 or num == prev_no - 1:
            count += 1
            if count >= 3:
                return False  # means consecutive no
        else:
            count = 1
        prev_no = num

    return True


#
print(is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]))
print(is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]))
# print(is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]))
# print(is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]))
print(is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]))


def eve_sum(lst):
    even_count = 0
    odd_count = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_count += lst[i]

        else:
            odd_count += lst[i]

    return [even_count, odd_count]


print(eve_sum([-1, -2, -3, -4, -5, -6]))
