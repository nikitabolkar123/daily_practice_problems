# Create a function that takes in a word and determines whether or not it is plural. A plural word is one that ends in "s".
#
# Examples
# is_plural("changes") ➞ True
#
# is_plural("change") ➞ False
#
# is_plural("dudes") ➞ True
#
# is_plural("magic") ➞ False
def is_plural(str):
    if str[-1] == 's':
        return True
    return False


print(is_plural('dudes'))
