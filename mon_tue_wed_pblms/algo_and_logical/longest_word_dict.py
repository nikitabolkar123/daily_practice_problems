# 524. Longest Word in Dictionary through Deleting
# Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by
# deleting some of the given string characters. If there is more than one possible result, return the longest word with
# the smallest lexicographical order. If there is no possible result, return the empty string.
# Example 1:
# Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# Output: "apple"
# Example 2:
# Input: s = "abpcplea", dictionary = ["a","b","c"]
# Output: "a"

def find_longest_word(s, dictionary):
    longest_word = ""
    for word in dictionary:
        i = 0
        j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                j += 1
            i += 1
        if j == len(word):
            if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                longest_word = word
    return longest_word


s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]
result = find_longest_word(s, dictionary)
print(result)  # Output: "apple"
