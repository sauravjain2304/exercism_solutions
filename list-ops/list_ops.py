def append(list1, list2):
  return list1 + list2 
print(append([1, 2], [2, 3, 4, 5]))   

def concat(lists):
  lst = []
  for i in lists:
    lst = lst + i
  return lst 
print(concat([[1, 2], [3], [], [4, 5, 6]])) 

def filter(function, list):
  lst = []
  for i in list:
    if function(i):
      lst = lst + [i]
  return lst    
print(filter(lambda x: x % 2 == 1, [1, 2, 3, 5]))

def length(list):
  return len(list)
print(length([1, 2, 3, 4]))

def map(function, list):
  lst = []
  for i in list:
    lst += [function(i)]
  return lst
print(map(lambda x: x + 1, [1, 3, 5, 7]))

def foldl(function, list, initial):
  for i in list:
    initial = function(initial, i)
  return initial 
print(foldl(lambda x, y: x + y, [1, 2, 3, 4], 5))   

def foldr(function, list, initial):
  for i in list[::-1]:
    initial = function(i, initial)
  return initial 
print(foldr(lambda x, y: x + y, [1, 2, 3, 4], 5))   

def reverse(list):
  return list[::-1] 
print(reverse([[1, 2], [3], [], [4, 5, 6]]))  