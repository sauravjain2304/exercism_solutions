def rows(letter):
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  length = letters.index(letter)
  result = []
  for num in range(length+1):
    string = " " * (length - num)
    string += letters[num]
    if num > 0:
      string += " " * ((num * 2) - 1)
      string += letters[num]
    string += " " * (length - num)
    result.append(string)
  for row in result[:-1][::-1]:
    result.append(row)
  return result
print(rows("D"))