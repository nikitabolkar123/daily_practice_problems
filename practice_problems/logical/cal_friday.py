"""
# "Create a function which returns how many Friday 13ths there are in a given year.
# Examples
# how_unlucky(2020) ➞ 2
# how_unlucky(2026) ➞ 3
# how_unlucky(2016) ➞ 1"
"""

import datetime


def how_unlucky(year):
    unlucky_count = 0
    for month in range(1, 13):
        if datetime.date(year, month, 13).weekday() == 4:
            unlucky_count += 1
    return unlucky_count


# print(how_unlucky(''))
print(how_unlucky(2022))  # 2
print(how_unlucky(2026))  # 3
print(how_unlucky(2016))  # 1
