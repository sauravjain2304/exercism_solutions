def spiral_matrix(size):
  matrix = [[0]*size for row in range(size)]
  i = 0
  j = -1
  element = 1
  di = [0, 1, 0, -1]
  dj = [1, 0, -1, 0]
  for x in range(2*size - 1):
    for _ in range((2*size - x) // 2):
      i += di[x % 4]
      j += dj[x % 4]
      matrix[i][j] = element
      element += 1
  return matrix
