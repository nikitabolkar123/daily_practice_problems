# Write a Python function to get a string made of the first three characters of a specified string. If the length of
# the string is less than 3, return the original string.
#
# def first_three_char(input_str):
#     str = ""
#     for i in range(len(input_str) - 1):
#         if i  not in str:
#             input_str[0:4] += str[i]
#
#     return str
#
#
# print(first_three_char('nikita'))
def first_three_chars(input_str):
    if len(input_str) < 3:
        return input_str
    else:
        return input_str[:3]


print(first_three_chars('nikita'))



