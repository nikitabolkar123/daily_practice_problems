# Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers.
#
# Vowel	Number
# A	4
# E	3
# I	1
# O	0
# U	0
# Examples
# sum_of_vowels("Let\'s test this function.") ➞ 8
#
# sum_of_vowels("Do I get the correct output?") ➞ 10
#
# sum_of_vowels("I love edabit!") ➞ 12
# Notes
# Vowels are case-insensitive (e.g. A = 4 and a = 4).
# def sum_of_vowels(txt):
#     vowels = 'AEIOUaeiou'
#     sum_of_vowels = 0
#
#     for i in range(len(txt)):
#         if txt[i] in vowels:
#             if txt[i] in 'AE':
#                 value = 4
#             elif txt[i] in 'ei':
#                 value = 1
#             elif txt[i] in 'Oo':
#                 value = 0
#             else:
#                 value = 3
#             sum_of_vowels += value
#
#     return sum_of_vowels
#
#
# s = "Do I get the correct output."
# result = sum_of_vowels(s)
# print(result)


# def sum_of_vowels(text):
#     vowels = 'AEIOUaeiou'
#     vowel_values = {'A': 4, 'E': 3, 'I': 1, 'O': 0, 'U': 0, 'a': 4, 'e': 3, 'i': 1, 'o': 0, 'u': 0}
#
#     vowel_values_lst= [vowel_values[char] for char in text if char in vowels]
#
#     return sum(vowel_values_lst)
#

# s = "I love edabit"
# result = sum_of_vowels(s)
# print(result)


def sum_of_vowels(text):
    vowel_values = {'A': 4, 'E': 3, 'I': 1, 'O': 0, 'U': 0}
    text = text.upper()
    vowels = [char for char in text if char in vowel_values]
    return sum(vowel_values[char] for char in vowels)


print(sum_of_vowels("I love edabit"))


def finding_vowel(input_string):
    vowel_dict = {'A': 4, 'E': 3, 'I': 1, 'O': 0, 'U': 0}
    input_string = input_string.upper()
    sum = 0
    for i in vowel_dict:
        for j in input_string:
            if i == j:
                sum = sum + vowel_dict[i]
    return sum


print(finding_vowel("I love edabit"))
