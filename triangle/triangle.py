def equilateral(sides):

  if (0 not in sides) and len(set(sides)) == 1:
    return True
  else:
    return False
  # if ((0  not in sides) and (sides[0] + sides[1] >= sides[2]) and (sides[0] + sides[2] >= sides[1]) and (sides[1] + sides[2] >= sides[0])):
  #   if len(set(sides)) == 1:
  #     return True
  #   else:
  #     return False
  # else:    
  #   return False      
print(equilateral([0,0,0]))      

def isosceles(sides):
  sides = sorted(sides)
  if (0 not in sides) and (len(set(sides))) <= 2 and (sides[0] + sides[1] >= sides[2]):
    return True
  else:
    return False
  # if ((0  not in sides) and (sides[0] + sides[1] >= sides[2]) and (sides[0] + sides[2] >= sides[1]) and (sides[1] + sides[2] >= sides[0])):
  #   if len(set(sides)) <= 2:
  #     return True
  #   else:
  #     return False
  # else:    
  #   return False    
print(isosceles([4,4,4]))        


def scalene(sides):
  sides = sorted(sides)
  if (0 not in sides) and (len(set(sides))) == 3 and (sides[0] + sides[1] >= sides[2]):
    return True
  else:
    return False
  # if ((0  not in sides) and (sides[0] + sides[1] >= sides[2]) and (sides[0] + sides[2] >= sides[1]) and (sides[1] + sides[2] >= sides[0])):
  #   if len(set(sides)) == 3:
  #     return True
  #   else:
  #     return False
  # else:    
  #   return False

print(scalene([2,3,7]))
