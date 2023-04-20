# Create a function that takes a list of lists and return the length of the missing list.
# Examples
# find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]) ➞ 3
# find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]) ➞ 3
# find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]) ➞ 2
import datetime


def how_unlucky(year):
    unlucky_count = 0
    for month in range(1, 13):
        if datetime.date(year, month, 13).weekday() == 4:
            unlucky_count += 1
    return unlucky_count


s = ([5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1])
print(how_unlucky(s))
