#  Write a Python function to insert a string in the middle of a string. Go to the editor
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def insert_string_middle(str, string_to_insert):
    mid_index = len(str) // 2
    result = ''
    for i in range(len(str)):
        if i == mid_index:
            result += string_to_insert
        result += str[i]
    return result


print(insert_string_middle('[[]]<<>>', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))
