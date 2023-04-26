# 4. Create a function that returns True if two strings share the same letter pattern, and False otherwise.
# Examples
# same_letter_pattern("ABAB", "CDCD") ➞ True
# same_letter_pattern("ABCBA", "BCDCB") ➞ True
# same_letter_pattern("FFGG", "CDCD") ➞ False
# same_letter_pattern("FFFF", "ABCD") ➞ False

def same_letter_pattern(s1, s2):
    a = len(s1)
    b = len(s2)
    if a != b:
        return False
    dict = {}
    for i in range(len(s1)):
        if s1[i] not in dict:
            dict[s1[i]] = s2[i]
        elif dict[s1[i]] != s2[i]:
            return False
    return True


s1 = 'ABAB'
s2 = 'CDCD'
print(same_letter_pattern(s1, s2))
print(same_letter_pattern("ABCBA", "BCDCB"))
print(same_letter_pattern("FFGG", "CDCD"))
print(same_letter_pattern("FFFF", "ABCD"))
