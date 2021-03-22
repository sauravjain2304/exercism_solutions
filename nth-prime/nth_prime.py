def prime(number):
  i = 3
  prime_nums = [2]
  if number <= 0:
    raise ValueError("error")
  while True:
    if len(prime_nums) == number:
      return prime_nums[-1]
    for j in range(2,i):
      if i % j == 0:
        break
      if j == i-1:
        prime_nums.append(i)
    i += 1
print(prime(20))    