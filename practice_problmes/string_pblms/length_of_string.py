# Write a Python program to calculate the length of a string.

def string_len(str):
    s = len(str)
    return s


str = "njjnnjn"
print(string_len(str))


def string_length(str):
    count = 0
    for char in str:
        count += 1
    return count


str1 = "nikita bolkar"
print(string_length(str1))

