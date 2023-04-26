# Create a function that reorders the digits of each numerical element in a list based on ascending (asc) or
# descending (desc) order.
#
# Examples
# reorder_digits([515, 341, 98, 44, 211], "asc") ➞ [155, 134, 89, 44, 112]
#
# reorder_digits([515, 341, 98, 44, 211], "desc") ➞ [551, 431, 98, 44, 211]
#
# reorder_digits([63251, 78221], "asc") ➞ [12356, 12278]
#
# reorder_digits([63251, 78221], "desc") ➞ [65321, 87221]
#
# reorder_digits([1, 2, 3, 4], "asc")  ➞ [1, 2, 3, 4]
#
# reorder_digits([1, 2, 3, 4], "desc") ➞ [1, 2, 3, 4]
#
def reorder_digits(lst, direction):
    for i in range(len(lst)):
        digits = [int(d) for d in str(lst[i])]   # it will convert the number to a string and split the digits
        # we r sort the digits in ascending or descending order
        # if direction == "asc":
        #     digits.sort()
        if direction == "asc":
            for j in range(1, len(digits)):
                key = digits[j]
                k = j - 1
                while k >= 0 and digits[k] > key:
                    digits[k + 1] = digits[k]
                    k -= 1
                digits[k + 1] = key
        else:
            for j in range(len(digits)):
                for k in range(j + 1, len(digits)):
                    if digits[k] > digits[j]:
                        temp=digits[j]
                        digits[j]=digits[k]
                        digits[k]=temp

        lst[i] = int("".join([str(d) for d in digits]))

    return lst


print(reorder_digits([515, 341, 98, 44, 211],"asc"))