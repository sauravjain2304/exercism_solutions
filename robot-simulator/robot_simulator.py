# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"
Direction = ["NORTH", "EAST", "SOUTH", "WEST"]


class Robot:
  def __init__(self, direction=NORTH, x=0, y=0):
    self.direction = direction
    self.x = x
    self.y = y
    self.coordinates = x, y

  def move(self, string):
    for letter in string:
      index = Direction.index(self.direction)
      if letter == "L":
        index = index - 1
      elif letter == "R":
        index = index - 3
      elif letter == "A":
        if index == 0:
          self.y = self.y + 1
        elif index == 1:
          self.x = self.x + 1
        elif index == 2:
          self.y = self.y - 1
        elif index == 3:
          self.x = self.x - 1
      self.direction = Direction[index]
      self.coordinates = (self.x, self.y)
    return self.direction, self.coordinates
obj = Robot(WEST, 0, 0)
print(obj.move("A"))     