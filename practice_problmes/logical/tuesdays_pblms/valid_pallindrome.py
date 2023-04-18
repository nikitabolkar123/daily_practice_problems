# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
# numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
def is_palindrome(s):
    new_s = ""
    for i in range(len(s)):
        char = s[i]
        if char.isalnum():
            if char.isalpha():
                new_s += char.lower()  # converts the character to lowercase
            else:
                new_s += char
    return new_s == new_s[::-1]  # if the new_s string is equal to its reverse


s1 = "A man, a plan, a canal: Panama"
print(is_palindrome(s1))
s = "race a car"
print(is_palindrome(s))
