import random
class Cipher:
  def __init__(self, key=None):
    if key is None:
      key = ''
      for _ in range(100):
        key += chr(random.randint(ord('a'), ord('z')))
    self.key = key.lower()            

  def encode(self, text):
    e_code = self.key * (len(text)//len(self.key)+1)
    output = ''
    for i in range(len(text)):
      k = ord(e_code[i]) - ord('a')
      e = ord(text[i]) + k if ord(text[i]) + k <= ord('z') else ord(text[i]) + k - 26
      output += chr(e)
    return output 

  def decode(self, text):
    d_code = self.key * (len(text)//len(self.key)+1)
    output = ''
    for i in range(len(text)):
      k = ord(d_code[i]) - ord('a')
      d = ord(text[i]) - k if ord(text[i]) - k >= ord('a') else ord(text[i]) - k + 26
      output += chr(d)
    return output
obj = Cipher("aaaaaaaaaa")
print(obj.encode("aaaaaaaaaa"))