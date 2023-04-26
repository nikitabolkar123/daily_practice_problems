# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from
# magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
#
#
# Example
# 1:
#
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example
# 2:
#
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example
# 3:
#
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
def can_construct(ransomNote, magazine):
    for i in range(len(ransomNote)):
        char = ransomNote[i]
        if char not in magazine:
            return False
        magazine = magazine[:magazine.index(char)] + magazine[magazine.index(char) + 1:]
    return True


ransomNote = "aa"
magazine = "aab"
print(can_construct(ransomNote, magazine))
