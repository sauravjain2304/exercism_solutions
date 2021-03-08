"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
  if category == 0:
    if len(set(dice)) == 1:
      return 50
    else:
      return 0

  if category == 1:
    return dice.count(1) * 1

  if category == 2:
    return dice.count(2) * 2

  if category == 3:
    return dice.count(3) * 3  

  if category == 4:
    return dice.count(4) * 4  

  if category == 5:
    return dice.count(5) * 5  

  if category == 6:
    return dice.count(6) * 6

  if category ==  7:
    dice = sorted(dice)
    b = list(set(dice))
    if len(b) == 2:
      if dice.count(list(b)[0]) == 3 or dice.count(list(b)[0]) == 2: 
        return sum(dice)
      else:
        return 0
    else:
      return 0

  if category == 8:
    for i in dice:
      if dice.count(i) >= 4:
        return 4 * i
      else:
        return 0 

  if category == 9:
    dice = sorted(dice)
    if dice == [1,2,3,4,5]:
      return 30
    else:
      return 0  
    
  if category == 10:
    dice = sorted(dice)
    if dice == [2,3,4,5,6]:
      return 30
    else:
      return 0 

  if category == 11:
    return sum(dice)

print(score([1, 4, 4, 4, 4], 7))    