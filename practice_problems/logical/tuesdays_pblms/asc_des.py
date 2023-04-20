# Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:
#
# "Asc" returns a sorted list in ascending order.
# "Des" returns a sorted list in descending order.
# "None" returns a list without any modification.
# Examples
# asc_des_none([4, 3, 2, 1], "Asc" ) ➞ [1, 2, 3, 4]
#
# asc_des_none([7, 8, 11, 66], "Des") ➞ [66, 11, 8, 7]
#
# asc_des_none([1, 2, 3, 4], "None") ➞ [1, 2, 3, 4]
#
# def asc_desc(lst):
#     for i in range(len(lst)):
#         lst.sort()
#     return lst
#
#
#
# print(asc_desc([4, 3, 2, 1]))
#
def asc_des(lst, sort):
    if sort == "Ascending":
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] > lst[j]:
                    temp = lst[i]
                    lst[i] = lst[j]
                    lst[j] = temp
        return lst
    elif sort == "Descending":
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] < lst[j]:
                    temp = lst[i]
                    lst[i] = lst[j]
                    lst[j] = temp
        return lst
    else:
        return lst


print(asc_des([4, 3, 2, 1], "Ascending"))
print(asc_des([7, 8, 11, 66], "Descending"))
print(asc_des([1, 2, 3, 4], "None"))
