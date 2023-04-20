# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of
# 1's ' \ in the binary representation of i. Input: n = 2 Output: [0,1,1] Explanation: 0 --> 0 1 --> 1 2 --> 10
#
# Example 2:
#
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

def count_bits(n):
    ans = []
    for i in range(n + 1):
        count = 0
        while i > 0:
            count += i % 2
            i //= 2
        ans.append(count)
    return ans


n = 5
ans = count_bits(n)
print(ans)
