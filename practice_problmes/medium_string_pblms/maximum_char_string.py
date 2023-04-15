# Write a Python program to find the maximum number of characters in a given string.


def get_max_occuring_char(string):
    max_char = ''
    max_count = 0

    for i in range(len(string)):
        count = string.count(string[i])
        if count > max_count:
            max_count = count
            max_char = string[i]

    return max_char


print(get_max_occuring_char("Python: Get file creation and modification date/times"))
print(get_max_occuring_char("abcdefghijkbfff"))
