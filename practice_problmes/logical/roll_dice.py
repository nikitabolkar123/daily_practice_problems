# 1.John is playing a dice game. The rules are as follows.
# Roll two dice.
# Add the numbers on the dice together.
# Add the total to your overall score.
# Repeat this for three rounds.
# But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!
#
# Create a function that takes in a list of tuples as input, and return John's score after his game has ended.
#
# Examples
# dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21
#
# dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0
# dice_game([(4, 5), (4, 5), (

def roll_dice(lst):
    score = 0
    i = 0
    while i < len(lst) and lst[i][0] != lst[i][1]:
        score += sum(lst[i])  # add  sum
        i += 1
    return score if i == len(lst) else 0  # if not double return score


print(roll_dice([(1, 2), (3, 4), (5, 6)]))

# def roll_dice(lst):
#     rolls = [sum(roll) for roll in lst if roll[0] != roll[1]]
#     score = sum(rolls)
#     return score if len(rolls) == len(lst) else 0
#
# print(roll_dice([(1, 2), (3, 4), (5, 6)]))
