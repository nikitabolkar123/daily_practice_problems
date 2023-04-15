# Write a Python program to remove punctuation from a given string.
def remove_punctuations(str):
    new_text = ""
    for char in str:
        if (33 <= ord(char) <= 47) or (58 <= ord(char) <= 64) \
                or (91 <= ord(char) <= 96) or (123 <= ord(char) <= 126):
            continue
        else:
            new_text += char
    return new_text


str = "String! With. #Punctuation!"
print(remove_punctuations(str))
