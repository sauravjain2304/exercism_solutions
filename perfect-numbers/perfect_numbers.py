def classify(number):
  aliquot_sum = 0
  if number < 1:
    raise ValueError("error")
  for n in range(1, number):
    if number % n == 0:
      aliquot_sum += n
  if aliquot_sum == number:
    return "perfect"
  elif aliquot_sum > number:
    return "abundant"
  else:
    return "deficient"
print(classify(12))