def sum_of_multiples(limit, multiples):
  factors = []    
  for n in range(1,limit):
    for m in multiples:
      val = n*m
      if val < limit and not val in factors:
        factors.append(val)
  return sum(factors)
print(sum_of_multiples(1000, [3, 5]))