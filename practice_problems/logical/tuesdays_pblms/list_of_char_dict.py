# Ques: 2
# Write a function that transforms a list of characters into a list of dictionaries, where:
#
# The keys are the characters themselves.
# The values are the ASCII codes of those characters.
# Examples
# to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]
# to_dict(["^"]) ➞ [{"^": 94}]
# to_dict([]) ➞ [].

def to_dict(lst):
    dict_list = []
    for i in range(len(lst)):
        dict_list.append({lst[i]: ord(lst[i])})
    return dict_list


print(to_dict(["a", "b", "c"]))
print(to_dict(["^"]))



