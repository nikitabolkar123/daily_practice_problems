# Someone has attempted to censor my strings by replacing every vowel with a , l*k th*s. Luckily, I've been able to
# find the vowels that were removed.
# Given a censored string and a string of the censored vowels, return the original uncensored string.
# Example
# uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
# uncensor("abcd", "") ➞ "abcd"
# uncensor("PP*RC*S", "UEAE") ➞ "UPPERCASE
def uncensor(string, vowels):
    uncensored = string
    for vowel in vowels:
        uncensored = uncensored.replace("*", vowel, 1)
    return uncensored


print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))  # "Where did my vowels go?"
print(uncensor("abcd", ""))  # "abcd"
print(uncensor("PP*RC*S", "UAE"))  # "UPPERCASE"
