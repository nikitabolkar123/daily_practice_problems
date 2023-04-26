# You are given three inputs: a string, one letter, and a second letter.
#
# Write a function that returns True if every instance of the first letter occurs before every instance of the second
# letter.
#
# Examples
# first_before_second("a rabbit jumps joyfully", "a", "j") ➞ True
# # Every instance of "a" occurs before every instance of "j".
#
# first_before_second("knaves knew about waterfalls", "k", "w") ➞  True
#
# first_before_second("happy birthday", "a", "y") ➞ False
# # The "a" in "birthday" occurs after the "y" in "happy".
#
# first_before_second("precarious kangaroos", "k", "a") ➞ False
# Notes
# All strings will be in lower case.
# All strings will contain the first and second letters at least once.
def first_before_second(txt, first, second):
    first_occurrence = None
    second_occurrence = None
    for i in range(len(txt)):
        if txt[i] == first:
            first_occurrence = i
            if second_occurrence is not None and first_occurrence > second_occurrence:
                return False
        elif txt[i] == second:
            second_occurrence = i
            if first_occurrence is not None and second_occurrence < first_occurrence:
                return False
    return True


print (first_before_second("happy birthday", "a", "y"))
print(first_before_second("knaves knew about waterfalls", "k", "w"))
print(first_before_second("a rabbit jumps joyfully", "a", "j"))