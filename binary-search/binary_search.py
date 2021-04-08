def find(search_list, value):
  if value > max(search_list):
    raise ValueError("error")
  elif value < min(search_list):
    raise ValueError("error")
  else:
    start = 0
    end = len(search_list)
    while start < end:
      midpoint = (start + end) // 2
      if search_list[midpoint] < value:
        start = midpoint + 1
      elif search_list[midpoint] > value:
        end = midpoint
      else:
        return midpoint
    raise ValueError("error")
print(find([1, 3, 4, 6, 8, 9, 11], 6))