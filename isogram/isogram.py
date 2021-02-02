def is_isogram(string):
  string = string.replace(" ","").replace("-","")
  old_size = len(string.lower())
  new_size = len(set(string.lower()))
  return old_size == new_size