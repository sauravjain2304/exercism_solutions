def abbreviate(words):
  words = words.replace("-"," ").replace("_"," ").split(" ")
  while '' in words:
    words.remove('')
  add = ""
  for x in words:
    add += x[0].upper()
  
  return(add)  