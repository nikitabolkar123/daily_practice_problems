# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# Example 1:
#
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.
# Example 2:
#
# Input: num = 0
# Output: 0
def repeatedly_add(num):
    while len(str(num)) > 1:
        number = 0
        for n in str(num):
            number += int(n)
        num = number
    return num


print(repeatedly_add(57)) #5+7=12 --1+2=3
