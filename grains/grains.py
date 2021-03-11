def square(number):
  if number <= 0 or number > 64:
    raise ValueError("error")
  return 2 ** (number - 1)

print(square(64))

def total():
  return 2**64 - 1