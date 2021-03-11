def flatten(iterable):
  finallist = []
  for element in iterable:
    print(finallist, element)
    if isinstance(element,(list,tuple)):
      finallist += flatten(element)
      print(finallist)
    elif element is not None:
      finallist += [element]
      print(finallist)
  return finallist    