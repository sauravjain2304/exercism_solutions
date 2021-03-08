def rotate(text, key):
  a = ""
  for ch in text:
    if ord(ch) == 32:
      a += ch
    elif ord(ch) == 39:
      a += ch  
    elif ord(ch) == 33:
      a += ch
    elif ord(ch) == 44:
      a += ch    
    elif ord(ch) == 46:
      a += ch  
    elif ch.isnumeric():
      a += ch  
    elif ch.isalpha():
      alphabet = ord(ch) + key
      if ch == ch.lower():
        if alphabet > ord('z'):
          alphabet -= 26
      else: 
        if alphabet > ord('Z'):
          alphabet -= 26 
      final = chr(alphabet)
      a += final
  return a        