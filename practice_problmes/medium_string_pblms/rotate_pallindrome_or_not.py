# Check if a string is a rotated palindrome or not
# Given a string, check if it is a rotated palindrome or not.
def is_rotated_palindrome(s):
    if s == s[::-1]:
        return True
    n = len(s)
    for i in range(1, n):
        rotated = s[i:] + s[:i]
        if rotated == rotated[::-1]:
            return True
    return False


s="CBAABCD"
s1="CBAABCEF"
print(is_rotated_palindrome(s1))