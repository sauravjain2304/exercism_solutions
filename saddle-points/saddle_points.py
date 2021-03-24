def saddle_points(matrix):
  rt = []
  row = []
  if matrix ==[]:
    return []
  if len(matrix) != 1:
    if len(matrix[0]) != len(matrix[1]):
      raise ValueError("error")  
  for x in range(len(matrix[0])):    
    l = []
    for y in range(len(matrix)):
      l.append(matrix[y][x])
    row.append(l)
  for x in range(len(matrix)):
    for y in range(len(matrix[0])):
      if matrix[x][y] == max(matrix[x]) and matrix[x][y] == min(row[y]):
        rt.append({"row": x+1, "column": y+1})
  return rt          
print(saddle_points([[4, 5, 4], [3, 5, 5], [1, 5, 4]]))