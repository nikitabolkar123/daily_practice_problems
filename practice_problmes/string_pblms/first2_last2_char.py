
# . Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'

def get_str(str):
    if len(str) < 2:
        return " "
    return str[0:2] + str[-2:]


print(get_str('w3resource'))
print(get_str('w3ce'))
print(get_str('w'))
