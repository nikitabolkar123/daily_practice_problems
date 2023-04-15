# Write a Python program to change a given string to a newly string where the first and last chars have been
# exchanged.

def change_string(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]


print(change_string('abcd'))
print(change_string('12345'))


# Write a Python script that takes input from the user and displays that input back in upper and lower cases. Go to
# the editor

def cases(str):
    upper_case=str.upper()
    lower_case=str.lower()
    return upper_case,lower_case


str = input('enter the string')
print(cases(str))
