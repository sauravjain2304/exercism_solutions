def encode(message, rails):
  memory = [[] for i in range(rails)]
  msg = [i for i in message if i.isalnum()]
  rail = 0
  for i in range(len(msg)):
    if rail == 0:
      direction = 1
    elif rail == rails - 1:
      direction = -1
    memory[rail].append(msg[i])
    rail += direction
  result = []
  for i in memory:
    result.extend(i)
  return ''.join(result)
print(encode("XOXOXOXOXOXOXOXOXO", 4))

def decode(encoded_message, rails):
  memory = [[] for i in range(rails)]
  msg = list(encoded_message)
  count = {i: 0 for i in range(rails)}
  rail = 0
  for i in range(len(msg)):
    if rail == 0:
      direction = 1
    elif rail == rails - 1:
      direction = -1
    count[rail] += 1
    rail += direction
  j = 0
  for i in range(rails):
    memory[i].extend(msg[j:j + count[i]])
    j += count[i]
  result = []
  rail = 0
  for i in range(len(msg)):
    if rail == 0:
      direction = 1
    elif rail == rails - 1:
      direction = - 1
    result.append(memory[rail].pop(0))
    rail += direction
  return ''.join(result)
print(decode("XXXXXXXXXOOOOOOOOO", 4))