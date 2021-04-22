def steps(number):
  if number <= 0:
    raise ValueError('error')
  step = 0
  while True:
    if number == 1:
      return step
    if number % 2:
      number = 3 * number + 1
    else:
      number = number / 2
    step = step + 1       
print(steps(16))    