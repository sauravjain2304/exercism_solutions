def largest(min_factor, max_factor):
  if min_factor > max_factor:
    raise ValueError("error")
  product = 0
  factors = []
  for x in range(max_factor, min_factor-1, -1):
    for y in range(x, min_factor-1, -1):
      p = x * y
      if p < product:
        break
      elif p == product and factors:
        factors.append((x, y))
        break
      elif p > product and str(p) == str(p)[::-1]:
        product, factors = p, [(x, y)]
        break
  if factors == []:
    return None, []
  else:
    return product, factors
print(largest(1, 9))    

def smallest(min_factor, max_factor):
  if min_factor > max_factor:
    raise ValueError("error")
  product = max_factor ** 2
  factors = []
  for x in range(min_factor, max_factor+1):
    for y in range(x, max_factor+1):
      p = x * y
      if p > product:
        break
      elif p == product and factors:
        factors.append((x, y))
        break
      elif p < product and str(p) == str(p)[::-1]:
        product, factors = p, [(x, y)]
        break
  if factors == []:
    return None, []
  else:
    return product, factors
print(smallest(10, 99))    