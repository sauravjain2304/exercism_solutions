def total(basket):
  prices = [800, 1520, 2160, 2560, 3000]
  result = []
  while basket:
    group = set(basket)
    result.append(len(group))
    for book in group:
      basket.remove(book)
  while 3 in result and 5 in result:
    result.remove(3)
    result.remove(5)
    result += [4, 4]
  return sum(prices[group] for group in result)
print(total([]))