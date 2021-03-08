def decode(string):
  mul = []
  result = []
  for c in string:
    if c.isdigit():
      mul.append(c)
    else:
      result.append(c * int(''.join(mul) or 1))
      mul.clear()
  return ''.join(result)

def encode(string):
  if not string:
    return ""
  result = []
  char = string[0]
  count = 0
  for c in string + "#":  
    if c == char:
      count += 1
    else:
      if count > 1:
        result.append(str(count))
      result.append(char)
      char = c
      count = 1
  return ''.join(result)