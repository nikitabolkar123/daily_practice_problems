"""
# "Create a function that takes an array of numbers and return ""Boom!"" if the digit 7 appears in the array. Otherwise,
# return ""there is no 7 in the array"".
# Examples
# sevenBoom([1, 2, 3, 4, 5, 6, 7]) ➞ ""Boom!""
# // 7 contains the number seven.
# sevenBoom([8, 6, 33, 100]) ➞ ""there is no 7 in the array""
# // None of the items contain 7 within them.
# sevenBoom([2, 55, 60, 97, 86]) ➞ ""Boom!""
# // 97 contains the number seven."
"""


def seven_boom(arr):
    for num in arr:
        if '7' in str(num):
            return "Boom!"
    if 7 in arr:
        return "Boom!"
    return "there is no 7 in the array"


print(seven_boom([2, 55, 60, 98, 86]))
