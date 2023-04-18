# "Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise, two
# lines rhyme if the last word from each sentence contains the same vowels.
# Examples
# does_rhyme(""Sam I am!"", ""Green eggs and ham."") ➞ True
# # Capitalization and punctuation should not matter.
# does_rhyme(""You are off to the races"", ""a splendid day."") ➞ False
# does_rhyme(""and frequently do?"", ""you gotta move."") ➞ F

def does_rhyme(s1, s2):
    vowels = "aeiouAEIOU"
    # Get the last word of each sentence
    s1_last_word = s1.split()[-1].lower()
    s2_last_word = s2.split()[-1].lower()
    # we r finding  the last vowel in each word
    s1_last_vowel = ""
    s2_last_vowel = ""
    for char in s1_last_word[::-1]:
        if char in vowels:
            s1_last_vowel = char
            break
    for char in s2_last_word[::-1]:
        if char in vowels:
            s2_last_vowel = char
            break
    return s1_last_vowel == s2_last_vowel  # Check if the last vowels are the same


print(does_rhyme("Sam I am!", "Green eggs and ham."))
print(does_rhyme("and frequently do?", "you gotta move."))
