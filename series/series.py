def slices(series, length):
  if length > len(series):
    raise ValueError("error")
  if length < 1:
    raise ValueError("error")
  lst = []
  for i in range(len(series) - length + 1):
    lst.append(series[i : length + i])
  return lst
print(slices("49142", 3))  