# str1 = input('enter the string')
# for i in range(len(str1)):
#     for j in range(i + 1, len(str1) + 1):
#         print(str1[i:j], end="  ")
#     print()

def substring(str):
    substrings = []
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            substrings.append(str[i:j])
    return substrings


print(substring('abc'))
