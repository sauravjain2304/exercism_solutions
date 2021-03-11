def largest_product(series, size):
  if len(series) < size:
    raise ValueError("error")
  if size < 0:
    raise ValueError("error")
  largest = 0
  for i in range(len(series) - size + 1):
    t = 1
    for j in range(size):
      t = t * int(series[i + j])
    if t > largest:
      largest = t
  return largest      
print(largest_product("1027839564", 3)) 