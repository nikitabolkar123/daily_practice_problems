# Create a function that takes a string (a random name). If the last character of the name is an "n", return True,
# otherwise return False.
#
# Examples
# is_last_character_n("Aiden") ➞ True
#
# is_last_character_n("Piet") ➞ False
#
# is_last_character_n("Bert") ➞ False
#
# is_last_character_n("Dean") ➞ True

def is_last_character_n(str):
    for i in str:
        if i in str:
            if str[-1] == 'n':
                return True
            return False


print(is_last_character_n("Piet"))


def is_last_character_n(name):
    if name[-1] == 'n':
        return True
    else:
        return False
