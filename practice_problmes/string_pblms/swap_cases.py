# 4. Write a Python program to swap cases in a given string. Go to the editor
# Sample Output:
# pYTHON eXERCISES
# jAVA
# nUMpY
# def swap_case_string(str1):
#     result_str = ""
#     for item in str1:
#         if item.isupper():
#             result_str += item.lower()
#         else:
#             result_str += item.upper()
#     return result_str
#
#
# print(swap_case_string("Nikita Bolkar"))


def swap_case_string(str1):
    result_str = ""
    for i in range(len(str1)):
        if str1[i].isupper():
            result_str += str1[i].lower()
        else:
            result_str += str1[i].upper()
    return result_str


print(swap_case_string("Nikita Bolkar"))



def swap_case_str(str1):
    result_lst = [ch.lower() if ch.isupper() else ch.upper() for ch in str1]
    return "".join(result_lst)


print(swap_case_string("Nikita Bolkar"))
