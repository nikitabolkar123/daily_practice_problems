# Create a function that takes a number (from 1 - 60) and returns a corresponding string of hyphens.
#
# Examples
# num_to_dashes(1) ➞ "-"
#
# num_to_dashes(5) ➞ "-----"
#
# num_to_dashes(3) ➞ "---"
# Notes
def num_to_dashes(num):
    return '-' * num


print(num_to_dashes(5))
