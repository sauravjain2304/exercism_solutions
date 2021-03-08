def factors(value):     
  pf = []
  factor = 2
  while value > 1:
    if value % factor == 0:
      pf.append(factor)
      value = value / factor
    else:
      factor += 1
  return pf  
print(factors(252))
