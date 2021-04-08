def transpose(lines):
  lines = lines.split('\n')
  result = []
  a = 0
  for line in lines:
    for i in range(len(line)):
      if i >= len(result):
        result.append("")
      if len(result[i]) < a:
        result[i] += " " * (a - len(result[i]))
      result[i] += line[i] 
    a += 1
  return '\n'.join(result)
# print(transpose("The first line.", "The second line."))  