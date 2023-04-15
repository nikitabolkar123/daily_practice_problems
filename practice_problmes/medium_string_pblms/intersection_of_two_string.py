# Write a Python program to find the common values that appear in two given strings.
def intersection_of_two_string(str1, str2):
    result = ""
    for i in range(len(str1)):
        ch = str1[i]
        if ch in str2 and ch not in result:
            result += ch
    return result


str1 = 'Python3'
str2 = 'Python2.7'
print(intersection_of_two_string(str1, str2))
