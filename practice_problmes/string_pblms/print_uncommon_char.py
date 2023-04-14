# Write a Python program that concatenates uncommon characters from two strings.

def uncommon_chars_concat(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    common_char = list(set1 & set2)
    res = [ch for ch in str1 if ch not in common_char] + [ch for ch in str2 if ch not in common_char]
    return ''.join(res)


str1 = 'abcdpqr'
str2 = 'xyzabcd'

print(uncommon_chars_concat(str1, str2))
