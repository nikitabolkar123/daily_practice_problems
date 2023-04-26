# Your task, is to create N x N multiplication table, of size n provided in parameter.
# For example, when n is 5, the multiplication table is:
# 1, 2, 3, 4, 5
# 2, 4, 6, 8, 10
# 3, 6, 9, 12, 15
# 4, 8, 12, 16, 20
# 5, 10, 15, 20, 25
# This example will result in:
#
# [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
# Examples
# multiplication_table(1) ➞ [[1]]

# multiplication_table(3) ➞ [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
def mul_table(n):
    mul_table = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
    return mul_table


tbl = mul_table(3)
print(tbl)


def mul(n):
    empty_table= []
    for i in range(1, n + 1):
        row = []
        for j in range(i, i + 1):
            row.append(i * j)
        empty_table.append(row)
    return empty_table
