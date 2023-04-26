# Determine whether a string can be transformed into another string in a single edit Given two strings,
# determine whether the first string can be transformed into the second string with a single edit operation. An edit
# operation can insert, remove, or replace a character in the first string.
# Input:  xyz —> xz
# Output: True
# Explanation: The total number of edits required is 1 (remove y from the first string)
# Input:  xyz —> xyyz
# Output: True
# Explanation: The total number of edits required is 1 (add y in the first string)

# Input: xyz — > xxx
# Output: False
# Explanation: The total number of edits required are 2 (replace y and z in thefirst string by x)
# Input:  xyz —> xyz
# Output: False
# Explanation: The total number of edits required is 0 (both strings are the same)

def is_single_edit_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    edit = False
    i = j = 0

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edit:
                return False

            edit= True

            if len(s1) > len(s2):
                i += 1
            elif len(s1) < len(s2):
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    return True


s1 = "xyz"
s2 = "xz"
result = is_single_edit_away(s1, s2)
print(result)

# #

