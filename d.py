def calculator():
  
  a = int(input("Enter first number: "))  
  b = int(input("Enter second number: ")) 
  c = input("enter a math operation ")
  if c =='+':
    c = a + b
  elif c =='-':
    c = a - b
  elif c =='*':
    c = a * b 
  elif c == '/':
    try:
      print(f"{a} / {b} is {a/b}")
      c = a / b
    except ZeroDivisionError:
      print("Cannot divide by zero")
      c = 0  
    # if b != 0:
    #   c = a / b
    # else:
    #   c = 0
  else:
    print("Invalid Input")
  return(c)
c = calculator()
print("number is", c)

class Matrix:
  def __init__(self, matrix_string):
    self.a = matrix_string

  def row(self, index):
    nums = self.a.split("\n")
    return list(map(int, nums[index - 1].split()))      
    # print(f"{nums}")
    # n = int(len(nums) ** 0.5)
    # return list(map(list, zip(*[map(int, nums)] * n)))
     
  def column(self, index):
    nums = self.a.split("\n")
    col = []
    for i in nums:
      col.append(i.split()[index - 1])
    # print(" ".join(map(str, col)))
    return list(map(int, col))

# m = Matrix("9 8 7\n5 3 2\n6 6 7")
# for i in [1, 2, 3]:
#   print(m.row(i))
# print(m.column(1))

# c = Matrix()



# import string
# def count_words(sentence):
#   output = ''
#   for char in sentence:
#     if char not in string.punctuation:
#       output += char
#   word_list1= output.split()
#   counter = {}
#   for word in word_list1:
#     if word in counter.keys():
#       counter[word] += 1
#     else:
#       counter[word] = 1
#   return counter
# print(count_words('the quick brown fox jumps over the lazy dog.'))



class School:
    def __init__(self):
        self.grades = {}

    def add_student(self, name, grade):
        self.grades.setdefault(grade, []).append(name)

    def roster(self):
        return [student for _, grade in sorted(
            self.grades.items()) for student in sorted(grade)]

    def grade(self, grade_number):
        return sorted(self.grades.get(grade_number, []))





class Clock:
    # The clock holds the hour for a 24 hour clock and minutes.
    def __init__(self, hour, minute):
        self.hour = (hour + minute//60) % 24
        self.minute = minute % 60

    def __repr__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    # Method __eq__ checks if other is the time equivalent of self
    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    # Method __add__ adds minutes to self
    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    # Method __sub__ subtracts minutes from self
    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)        


# sentence = sentence.lower()

#     for ch in alphabet:
#         if ch not in sentence:
#             return False

#     return True 



word = word.lower()
    sorted_word = sorted(word)
    def is_anagram(candidate):
        candidate = candidate.lower()
        return sorted_word == sorted(candidate) and word != candidate
    return list(filter(is_anagram, candidates))



    if self.score in self.d.keys() and item == self.d[self.score]:
      return True
    else:
      x = [x for x in self.d.keys() if x < self.score]
      # print(x)
      x = [self.d[i] for i in x]
      if item in x:
        return True
      else:
        return False
      return False   