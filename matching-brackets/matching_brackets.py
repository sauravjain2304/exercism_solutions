def is_paired(input_string):
  pairs = {")": "(", "]": "[", "}": "{"}
  result = []
  for i in input_string:
    if i in "([{":
      result.append(i)
    elif i in ")]}":
      if not result or result[-1] != pairs[i]:
        return False
      result.pop()
  return not result
print(is_paired("{[]}"))  