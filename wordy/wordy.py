def answer(question):
  question = question.replace('by ', '')
  fields = question[8:-1].split(' ')
  while len(fields) > 1:
    operation = fields[1]
    if len(fields) < 3:
      raise ValueError("error")
    elif operation == 'plus':
      fields[2] = int(fields[0]) + int(fields[2])
      fields = fields[2:]
    elif operation == 'minus':
      fields[2] = int(fields[0]) - int(fields[2])
      fields = fields[2:]
    elif operation == 'multiplied':
      fields[2] = int(fields[0]) * int(fields[2])
      fields = fields[2:]
    elif operation == 'divided':
      fields[2] = int(fields[0]) // int(fields[2])
      fields = fields[2:]
    else:
      raise ValueError("error")
  return int(fields[0])
print(answer("What is 53 plus 2?"))