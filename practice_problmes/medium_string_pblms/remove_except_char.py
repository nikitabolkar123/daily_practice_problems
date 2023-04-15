# Write a Python program to remove all characters except a specified character from a given string.
def remove_characters(str1, c):
    return ''.join([ele for ele in str1 if ele == c])


text = "google"
except_char = "o"
print("Remove all characters except", except_char)
print(remove_characters(text, except_char))
