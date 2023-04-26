# Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or phrase
# formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly
# once.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example
# 2:
#
# Input: s = "rat", t = "car"
# Output: false

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    char_count = {}
    for char in s:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True


s = "anagram"
t = "nagaram"
print(is_anagram(s, t))  # Output: True
