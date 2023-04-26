# Check if a repeated subsequence is present in a string or not Given a string, check if a repeated subsequence is
# present in it or not. The repeated subsequence should have a length of 2 or more.
def repeated_subsequence(str):
    n = len(str)
    dp = [[0] * n for _ in range(n)]  # dp is a 2D array of size n x n initialize to all zeros

    for i in range(n):
        for j in range(i + 1, n):
            if str[i] == str[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            if dp[i][j] >= 2:
                return True

    return False


string1 = "XYBAXB"
print(repeated_subsequence(string1))

string2 = "XBXAXB"
print(repeated_subsequence(string2))

string3 = "ABCA"
print(repeated_subsequence(string3))

string4 = "XYBYAXBY"
print(repeated_subsequence(string4))
