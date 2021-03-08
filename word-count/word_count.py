import re
def count_words(sentence):
  
  counts = dict()
  # counts = counts.replace(" ","").replace("\n","")
  sentence = re.sub(r"^'|\s'|'\s|'$", " ", sentence)
  sentence = re.sub(r"^'|\s'|'\s|'$", " ", sentence)
  sentence = sentence.replace("\n"," ").replace(","," ").replace("_"," ")
  sentence = sentence.replace("."," ").replace(":"," ").replace("!!&@$%^&"," ").replace(",\n"," ").lower()
  words = sentence.split()
  print(words)
  for word in words:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1
  return counts
print( count_words('the quick brown fox jumps over the lazy dog.'))
