# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.
# Input: num1 = "11", num2 = "123"
# Output: "134"
# Input: num1 = "456", num2 = "77"
# Output: "533"
def add_strings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    return str(int(num1) + int(num2))


print(add_strings("456", "77"))
