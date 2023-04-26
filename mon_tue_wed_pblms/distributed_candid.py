# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight,
# so she visited a doctor.
# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very
# much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.
# Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if
# she only eats n / 2 of them.
# Example 1:
#
# Input: candyType = [1,1,2,2,3,3]
# Output: 3
# Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
# Example 2:
#
# Input: candyType = [1,1,2,3] Output: 2 Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [
# 1,2], [1,3], or [2,3], she still can only eat 2 different types. Example 3:
#
# Input: candyType = [6,6,6,6]
# Output: 1
# Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.
# def max_num_of_different_types(candy_type):
#     unique_types = {}
#     for candy in candy_type:
#         if candy not in unique_types:
#             unique_types[candy] = 1
#         else:
#             unique_types[candy] += 1
#
#     return min(len(unique_types), len(candy_type) // 2)
#
#
# candy_type =[1,1,2,3]
# print(max_num_of_different_types(candy_type))
