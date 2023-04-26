# Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better
# understanding:
#
# Examples
# fact_of_fact(4) ➞ 288
# # 4! * 3! * 2! * 1! = 288
#
# fact_of_fact(5) ➞ 34560
#
# fact_of_fact(6) ➞ 24883200
def fact_of_fact(n):
    res = 1
    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact = fact * j
        res *= fact
    return res


print(fact_of_fact(4))
print(fact_of_fact(5))
print(fact_of_fact(6))


#
# Create a function that counts the number of digits in a number. Conversion of the number to a string is not allowed.
#
# Examples
# digits_count(4666) ➞ 4
#
# digits_count(544) ➞ 3
#
# digits_count(121317) ➞ 6
#
# digits_count(0) ➞ 1
#
# digits_count(12345) ➞ 5
#
# digits_count(1289396387328) ➞ 13
# Notes
# All inputs are integers but some are in exponential form, deal with it accordingly.
def digits_count(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10

    return count


#
# print(digits_count(1234))
# print(digits_count(1289396387328))
#
#
# #
#
# 3.Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.
#
# Examples
# next_prime(12) ➞ 13
#
# next_prime(24) ➞ 29
#
# next_prime(11) ➞ 11
# 11 is a prime, so we return the number itself.

# print(next_prime(12))
def next_prime(n):
    if n < 2:
        return 2
    if n % 2 == 0:
        n += 1
    while True:
        for i in range(3, (n//2)+1, 2):
            if n % i == 0:
                break
        else:
            return n
        n += 2


print(next_prime(12))
print(next_prime(24))
print(next_prime(11))
