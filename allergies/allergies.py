from itertools import combinations
import itertools
class Allergies:
  def __init__(self, score):
    self.score = score
    self.d = {1: "eggs", 2: "peanuts", 4: "shellfish", 8: "strawberries", 16: "tomatoes", 32: "chocolate", 
             64: "pollen", 128: "cats" }
    self.lst = self.score
    
  def allergic_to(self, item):
    if self.score in self.d.keys() and item == self.d[self.score]:
      return True
    else:
      if item in self.lst:    
        return True 
      else:
        return False
        
        
  @property
  def lst(self):
    return self._lst

  @lst.setter
  def lst(self, score):
    x = [x for x in self.d.keys() if x <= score]
    res = []
    for i in range(0, len(x) + 1):
      for p in list(combinations(x, i)):
        if sum(p) == score:
          res.append(list(p))
    if res == [] and sum(x) < score:
      old_score = score
      while old_score > 0:
        old_score = old_score - 256
        for i in range(0, len(x) + 1):
          for p in list(combinations(x, i)):
            if old_score == sum(p):
              res.append(list(p))
    t = list(itertools.chain.from_iterable(res))
    t = sorted(set(t))
    t = list(map(lambda x: self.d[x], t))
    self._lst = t


obj = Allergies(509)
# print(obj.allergic_to("eggs"))
print(obj.lst)