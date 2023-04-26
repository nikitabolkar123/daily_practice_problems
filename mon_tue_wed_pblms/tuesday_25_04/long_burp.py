# Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the
# function.
#
# Examples
# long_burp(3) ➞ "Burrrp"
#
# long_burp(5) ➞ "Burrrrrp"
#
# long_burp(9) ➞ "Burrrrrrrrrp"
# def long_burp(n):
#     r_string = "r" * n
#     return "Bu" + r_string + "p"
#
#
# print(long_burp(3))

def long_burp(n):
    return "".join(["Bu", "r" * n, "p"])


print(long_burp(3))
