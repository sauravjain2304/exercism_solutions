class Luhn:
  def __init__(self, card_num):
    self.card_num = card_num.replace(" ","")

  def valid(self):
    if len(self.card_num) <= 1:
      return False
    if not self.card_num.isdigit():
      return False 
    result = 0 
    digit = self.card_num
    digit = digit[::-1]
    for i in range(0, len(digit)):
      if i % 2 != 0:
        x = int(digit[i]) * 2
        if x > 9:
          x = x - 9
      else:
        x = int(digit[i])    
      result = result + x
        
    return result % 10 == 0
    
obj = Luhn("055-444-285")
print(obj.valid())

      


        


