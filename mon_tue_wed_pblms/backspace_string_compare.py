# 844. Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a
# backspace character.
# Note that after backspacing an empty text, the text will continue empty.
# Example 1:
#
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:
#
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:
#
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

def string_compare(s, t):
    i = len(s) - 1
    j = len(t) - 1
    backspaces_s = 0
    backspaces_t = 0

    while i >= 0 or j >= 0:
        while i >= 0 and (s[i] == '#' or backspaces_s > 0):         # it will skip backspaces in s
            if s[i] == '#':
                backspaces_s += 1
            else:
                backspaces_s -= 1
            i = i - 1

        # skip backspaces in t
        while j >= 0 and (t[j] == '#' or backspaces_t > 0):
            if t[j] == '#':
                backspaces_t += 1
            else:
                backspaces_t -= 1
            j = j - 1

        # Compare current characters
        if i >= 0 and j >= 0 and s[i] == t[j]:
            i = j - 1
            j = j - 1
        else:
            return i == j == -1

    return True


s = "a#c"
t = "b"
print(string_compare(s, t))
