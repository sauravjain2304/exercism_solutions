def encode(numbers):
  ret = []
  for n in reversed(numbers):
    a = 0
    while True:
      ret.append((n & 127) | a)
      a = 128
      n >>= 7
      if n == 0:
        break
  return list(reversed(ret))  
print(encode([0x2000]))   

def decode(bytes_):
  ret = []
  temp = 0
  for n in bytes_:
    temp = (temp << 7) | (n & 127)
    if not (n & 128):
      ret.append(temp)
      c = True
      temp = 0
    else:
      c = False
  if not c:
    raise ValueError()
  return ret       
print(decode([0xFF]))  