# Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# def max(s):
#     count=0
#     for i in range(len(s)):
#         if s[i]==s[-1]:
#             s[i]+=count
#

def length_of_last_word(s):
    if len(s) == 1 and s[0] != ' ':
        return 1
    n = len(s) - 1
    for i in range(n, -1, -1):
        if s[i] == ' ':
            if n - i != 0 and s[i + 1] != ' ':
                return n - i
            else:
                n = i - 1
        elif i == 0:
            return n - i + 1
    return 0


ss = " fly me   to   the moon"
print(length_of_last_word(ss))
