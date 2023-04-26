# Write a function that changes every letter to the next letter:
#
# "a" becomes "b"
# "b" becomes "c"
# "d" becomes "e"
# and so on ...
# Examples
# move("hello") ➞ "ifmmp"
# move("bye") ➞ "czf"
# move("welcome") ➞ "xfmdpnf"
def move(word):
    str = ''
    for i in range(len(word)):
        char = word[i]
        if char.isalpha():
            unicode = ord(char) + 1
            if char.isupper() and unicode > ord('Z'):
                unicode -= 26
            elif char.islower() and unicode > ord('z'):
                unicode -= 26
            str += chr(unicode)
        else:

            str += char  # if char not alpha then  append to new string
    return str


print(move("hello"))
print(move("bye"))
print(move("welcome"))
