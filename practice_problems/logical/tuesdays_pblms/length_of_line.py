# Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line
# segment connecting those two points.
#
# Examples
# line_length([15, 7], [22, 11]) ➞ 8.06
# line_length([0, 0], [0, 0]) ➞ 0
# line_length([0, 0], [1, 1]) ➞ 1.41
# Note:
# use operator for exponent value

import math


def line_length(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print(line_length((15, 7), (22, 11)))
print(line_length((0, 0), (0, 0)))
print(line_length((0, 0), (1, 1)))

# formula
# distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


#
# def line_length(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
