# Number to words
# Input: '123'
# Output: One Two Three
#
# Input: '1223'
# Output: One DoubleTwo Three
#
# Input: '123333'
# Output: One Two TripleThree


def num_to_words(num):
    dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    str_num = str(num)
    w = []
    i = 0
    while i < len(str_num):
        digit = int(str_num[i])
        count = 1
        while i + 1 < len(str_num) and str_num[i + 1] == str_num[i]:
            count += 1
            i += 1
        if count == 2:
            w.append("Double" + dict[digit])
        elif count == 3:
            w.append("Triple" + dict[digit])
        else:
            w.append(dict[digit])
        i += 1
    return ' '.join(w)


print(num_to_words(123))
print(num_to_words(12223777))
print(num_to_words(1233))
