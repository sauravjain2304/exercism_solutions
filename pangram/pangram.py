def is_pangram(sentence):
  letter = "abcdefghijklmnopqrstuvwxyz"
  only_alpha = ""
  for char in sentence:
    if char.isalpha():
      only_alpha += char
  sentence = ''.join(sorted(set(only_alpha.lower())))
 
  if letter == sentence:
    return True
  else:
    return False
  # for ch in letter:
    # if ch in letter:
      # return True
  # return False
print(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))      