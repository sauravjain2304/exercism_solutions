def is_armstrong_number(number):
  a = list(map(int,list(str(number))))
  result = 0
  for i in range(0, len(a)):
    b = a[i] ** len(a)
    result += b
  if result == number:
    return True
  else:
    return False
         