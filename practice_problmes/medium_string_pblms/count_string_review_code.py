# 4.Run–length encoding (RLE) is a simple form of lossless data compression that runs on sequences with the same value
# occurring many consecutive times. It encodes the sequence to store only a single value and its count.
#
# Input: 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
# Output: '12W1B12W3B24W1B14W'
# Explanation: String can be interpreted as a sequence of twelve W’s, one B, twelve W’s, three B’s, and so on..

def sequence_count(s):
    if not s:
        return ""
    count = 1
    str1 = ""
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1

        else:
            str1 += str(count) + \
                    s[i - 1]
            count = 1

    str1 += str(count) + s[-1]
    return str1


# s='WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
s = 'aaabcccd'
print(sequence_count(s))
