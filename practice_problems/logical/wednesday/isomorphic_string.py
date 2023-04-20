# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    s_dict={}
    t_dict = {}

    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = t[i]
        elif s_dict[s[i]] != t[i]:
            return False

        if t[i] not in t_dict:
            t_dict[t[i]] = s[i]
        elif t_dict[t[i]] != s[i]:
            return False

    return True


s = "egg"
t = "add"
print(is_isomorphic(s,t))