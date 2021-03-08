def roman(number):
  val = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
  res = ''
  for i in val:
    while number >= i:
      res = res + val[i]
      number = number - i
  return res
print(roman(3000))  