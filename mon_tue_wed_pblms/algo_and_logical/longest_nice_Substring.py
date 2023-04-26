# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and
# lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not
# because 'b' appears, but 'B' does not.
# Example 1:
#
# Input: s = "YazaAay" Output: "aAa" Explanation: "aAa" is a nice string because 'A/a' is the only letter of the
# alphabet in s, and both 'A' and 'a' appear. "aAa" is the longest nice substring. Example 2:
#
# Input: s = "Bb"
# Output: "Bb"
# Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
# Check if s is already nice
def longest_nice_substring(s):
    longest_nice = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            nice = True
            for c in sub:
                if c.lower() not in sub or c.upper() not in sub:
                    nice = False
                    break
            if nice and len(sub) > len(longest_nice):
                longest_nice = sub
    return longest_nice


s = "YazaAay"
result = longest_nice_substring(s)
print(result)
