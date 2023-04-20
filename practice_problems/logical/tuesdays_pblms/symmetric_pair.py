# Find all symmetric pairs in an array of pairs
# Given an array of pairs of integers, find all symmetric pairs, i.e., pairs that mirror each other. For instance, pairs
# (x, y) and (y, x) are mirrors of each other.
# Input: {3, 4}, {1, 2}, {5, 2}, {7, 10}, {4, 3}, {2, 5}
#
# Output:
#
# {4, 3} | {3, 4}
# {2, 5} | {5, 2}
def find_symmetric_pairs(arr):
    sym_pairs = set()
    dict = {}
    for pair in arr:
        first, second = pair
        if second in dict and dict[second] == first:
            sym_pairs.add((first, second))
            sym_pairs.add((second, first))
        else:
            dict[first] = second
    return sym_pairs


arr = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
res = find_symmetric_pairs(arr)
print(res)
