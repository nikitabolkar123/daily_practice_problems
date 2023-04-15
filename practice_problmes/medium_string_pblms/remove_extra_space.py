# Remove all extra spaces from a string

def remove_extra_spaces(s):
    res = ""
    prev_char = ""
    for i in range(len(s)):
        curr_char = s[i]
        if curr_char != " ":
            res += curr_char
            prev_char = curr_char
        elif prev_char != " ":
            res += curr_char
            prev_char = curr_char

    return res


s = "  This    is  a  string    with extra    spaces.  "
print(remove_extra_spaces(s))
