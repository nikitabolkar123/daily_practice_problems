# reverse string
# def reverse_str(string):
#     rev_str = ''
#     for char in string:
#         rev_str = char + rev_str
#     return rev_str
#
#
# str = 'nikita'
# print(reverse_str(str))
def reverse_str(string):
    rev_str = ''
    for i in range(len(string)-1, -1, -1):
        rev_str += string[i]
    return rev_str


str = 'nikita'
print(reverse_str(str))

