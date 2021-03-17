from math import sqrt, floor
def cipher_text(plain_text):
  text = "".join([x for x in plain_text.lower() if x.isalnum()])
  cipher_len = len(text)
  col = row = floor(sqrt(cipher_len))
  while col * row < cipher_len:
    if col > row:
      row += 1
    else:
      col += 1
  square = []
  for i in range(row):
    square.append(text[i * col : i * col + col].ljust(col))
  result = []
  for i in range(col):
    result.append("")
    for j in range(row):
      result[i] += square[j][i]
  return " ".join(result)
print(cipher_text("Chill out."))  