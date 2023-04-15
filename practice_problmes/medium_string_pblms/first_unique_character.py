# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#
# Example1:
#
# Input: s = "leetcode"
# Output: 0
# Example2:
#
# Input: s = "loveleetcode"
# Output: 2
# Example3:
#
# Input: s = "aabb"
# Output: -1

def first_uniq_char(s):
    for i in range(len(s)):
        c = s[i]
        if s.count(c) == 1:
            return i
    return -1


print(first_uniq_char('loveleetcode'))
