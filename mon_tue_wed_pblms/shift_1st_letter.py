# Given a sentence, create a function which shifts the first letter of each word to the next word in the sentence (shifting right).
#
# Examples
# shift_sentence("create a function") ➞ "freate c aunction"
#
# shift_sentence("it should shift the sentence") ➞ "st ihould shift she tentence"
#
# shift_sentence("the output is not very legible") ➞ "lhe tutput os iot nery vegible"
#
# shift_sentence("edabit") ➞ "edabit"
# Notes
# The last word shifts its first letter to the first word in the sentence.
# All sentences will be given in lowercase.
# Note how single words remain untouched (example #4).
# def shift_sentence(sentence):
#     words = sentence.split()
#     shifted_words = []
#     for i in range(len(words)):
#         word = words[i]
#         next_word_index = (i + 1) % len(words)
#         next_word = words[next_word_index]
#         if i == len(words) - 1:
#             shifted_word = next_word[0] + word[1:]
#         else:
#             shifted_word = word[1:] + next_word[0]
#         shifted_words.append(shifted_word)
#     return " ".join(shifted_words)
#

# sentence = "it should shift the sentence"
# shifted_sentence = shift_sentence(sentence)
# print(shifted_sentence)  # Output: "freate c aunction"
