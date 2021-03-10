def primes(limit):
  if limit < 2:
    return []
  primes = [2]
  for num in range(2,limit + 1):  
    for i in range(2,num):  
      if (num % i) == 0:  
        break  
      else:  
        if num not in primes:
          primes.append(num)
  return primes 
print(primes(10))  