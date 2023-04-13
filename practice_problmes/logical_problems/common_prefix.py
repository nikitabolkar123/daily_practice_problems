# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Input: strs = ["flower","flow","flight"]
# Output: "fl"d
def longest_common_prefix(str):
    if not str:
        return ""
    pref = str[0]
    for i in range(1, len(str)):
        j = 0
        while j < len(pref) and j < len(strs[i]) and pref[j] == strs[i][j]:
            j += 1
        pref = pref[:j]
        if not pref:
            return ""
    return pref


strs = ["flower", "flow", "flight"]
result = longest_common_prefix(strs)
print(result)
