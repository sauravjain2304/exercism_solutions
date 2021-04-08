def rectangles(strings):
  rec = 0
  for i in range(len(strings)):
    if '+' in strings[i]:
      for a in range(len(strings[i])):
        if strings[i][a] == '+':
          opened = a
          for c in range(a+1, len(strings[i])):
            if strings[i][c] == '+':
              closed = c
              for b in range(i + 1, len(strings)):
                if strings[b][opened] not in "+|" or strings[b][closed] not in "+|":
                  break
                if strings[b][opened] == "+" and strings[b][closed] == "+":
                  rec += 1
  return rec
print(rectangles(["  +-+", "  | |", "+-+-+", "| |  ", "+-+  "]))  