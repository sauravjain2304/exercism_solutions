def is_valid(isbn):
  isbn = isbn.replace('-', '')
  if len(isbn) != 10: 
    return False
  result = 0
  for i in range(len(isbn)):
    if isbn[i] == 'X':
      result = result + 10
    elif not isbn[i].isnumeric():
      return False
    else:
      result = result + int(isbn[i]) * (10 - i)    
  if result % 11 == 0:
    return True
  else:  
    return False
print(is_valid("359821507X"))         