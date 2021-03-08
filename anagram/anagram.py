def find_anagrams(word, candidates):
  result = []
  for i in candidates:
    if i.lower() != word.lower():
      if sorted(list(i.lower())) == sorted(list(word.lower())):
        result.append(i)
  return result       

