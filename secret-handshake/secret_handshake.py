def commands(number):
  digits = []
  remaining = number
  while remaining > 0:
    digits.append(remaining % 2)
    remaining //= 2
    print(digits)
  if len(digits) < 5:
    diff = 5 - len(digits)
    for i in range(0, diff):
      digits.append(0)
      print(digits)
  shake = []
  parts = ["wink", "double blink", "close your eyes", "jump"]
  for i in range(0, 4):
    if digits[i] == 1:
      shake.append(parts[i])
      print(shake)
  if digits[4] == 1:
    shake.reverse()
    print(shake)
  return shake
print(commands(15))  