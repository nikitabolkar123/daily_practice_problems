# Write a Python program to get a single string from two given strings, separated by a space and swap the first two
# characters of each string.
def swap_str(str1, str2):
    new_a = str2[:2] + str1[2:]
    new_b = str1[:2] + str1[2:]
    return new_a + ' ' + new_b


print(swap_str('abcnck', 'xmxjjn'))


#
# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string
# already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3,
# leave it unchanged. Go to the editor Sample String : 'abc' Expected Result : 'abcing' Sample String : 'string'
# Expected Result : 'stringly'

def string_len(str):
    length = len(str)
    if length > 2:
        if str[-3:] == 'ing':
            str += 'ly'
        else:
            str += 'ing'
    return str


print(string_len('ab'))
print(string_len('abc'))
print(string_len('string'))


# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not'
# follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the
# editor Sample String : 'The lyrics is not that poor!' 'The lyrics is poor!' Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
def substring(str):
    for char in range(len(str)):
        str[-1] = str[1]


#
# Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Go to the editor Sample Output: Longest word: Exercises Length of the longest word: 9
# def longest_word(str):
#     lst = []
#     for c in str:
#         lst.append((len(c), c))
#     lst.sort()
#     return lst[-1][0], lst[-1][-1]
#
#
# res = longest_word(['hii', 'good', 'morning'])
# print('length of words ', res[1])
# print('length of longest word', res[0])

def longest_word(str):
    lst = []
    for i in range(len(str)):
        lst.append((len(str[i]), str[i]))
    lst.sort()
    return lst[-1][0], lst[-1][-1]


res = longest_word(['hii', 'good', 'morning'])
print('length of words ', res[1])
print('length of longest word', res[0])



