# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
# Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# Example 2:
# Input: stones = [1]
# Output: 1
def lastStoneWeight(stones):
    stones.sort()
    while len(stones) > 1:
        y = stones.pop(-1)
        x = stones.pop(-1)
        if x != y:
            stones.append(y - x)
        stones.sort()
    if len(stones) >= 1:
        return stones[0]
    else:
        return 0


print(lastStoneWeight([2,7,4,1,8,1]))
