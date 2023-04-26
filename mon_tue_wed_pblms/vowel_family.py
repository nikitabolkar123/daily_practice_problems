# Write a function that selects all words that have all the same vowels (in any order and/or number) as the first
# word, including the first word.
# same_vowel_group(["toe", "ocelot", "maniac"]) ➞ ["toe", "ocelot"]
#
# same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) ➞ ["many"]
#
# same_vowel_group(["hoops", "chuff", "bot", "bottom"]) ➞ ["hoops", "bot", "bottom"]
# Notes
# Words will contain only lowercase letters, and may contain whitespaces. Frequency does not matter (e.g. if the
# first word is "loopy", then you can include words with any number of o's, so long as they only contain o's,
# and not any other vowels).
def same_vowel_group(words):
    vowels = set('aeiou')
    first_word_vowels = set(filter(lambda x: x in vowels, words[0]))
    result = [words[0]]

    for word in words[1:]:
        if set(filter(lambda x: x in vowels, word)) == first_word_vowels:
            result.append(word)

    return result


print(same_vowel_group(["hoops", "chuff", "bot", "bottom"]))
