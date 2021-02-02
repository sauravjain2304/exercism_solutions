def distance(strand_a, strand_b):
  result = 0
  if len(strand_a) != len(strand_b):
    raise ValueError("String are not equal")
  else:
    for i in range(0, len(strand_a)):
      if strand_a[i] != strand_b[i]:
        result += 1
  return result

# print(distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))