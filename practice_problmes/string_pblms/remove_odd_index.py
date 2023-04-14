# Write a Python program to remove characters that have odd index values in a given string.

def odd_values_string(str):
    res = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = res + str[i]
    return res


print(odd_values_string('abcdef'))
print(odd_values_string('python'))
