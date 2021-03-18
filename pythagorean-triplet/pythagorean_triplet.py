def triplets_with_sum(number):
  triplets = []
  for a in range(1, number // 3):
    for b in range(a + 1, number // 2):
      c = number - a - b
      if (a + b >= c) and (a ** 2 + b ** 2 == c ** 2):
        triplets.append([a, b, c])
  return triplets
print(triplets_with_sum(1000))