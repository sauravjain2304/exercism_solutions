def translate(sentance):
  text = list(sentance.split(" "))
  a = []
  for w in text:
    a += translates(w) + " "
  return ''.join(a).strip()
def translates(text):
  vowels = ['a','e','i','o','u']
  word = list(text)
  if word[0] in vowels:
    text = word + ['ay']
    return ''.join(text)
  elif ''.join(word[0:2]) in ['xr','yt']:
    text = word +['ay']
    return ''.join(text)  
  for i in range(len(word)):
    if word[i] in vowels:
      text = word[i:] + word[:i] + ['ay']
      break  
    elif word[i] == 'y':
      text = word[i:] + word[:i] + ['ay']
      # break 
    elif word[i] == 'q' and word[i + 1] == 'u':
      text = word[i+2:] + word[:i+2] + ['ay']
      break 
  return ''.join(text)