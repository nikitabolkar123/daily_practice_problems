#
#  Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
def count_character(str):
    dict = {}
    for i in range(len(str)):
        keys = dict.keys()
        if str[i] in keys:
            dict[str[i]] += 1
        else:
            dict[str[i]] = 1
    return dict

print(count_character('google.com'))
