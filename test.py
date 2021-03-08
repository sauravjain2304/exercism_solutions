

# class A:

#   def f1( self, abc):
#     self.abc = abc
#     print(abc)

#   def f2(self, abc):
#     print(abc)
#     print(self.abc)

# obj = A()
# obj.f1(1234)
# obj.f2(789)


# def fix(string):
#     s = set()
#     list = []
#     for ch in string:
#         if ch not in s:
#             s.add(ch)
#             list.append(ch)

#     return ''.join(list)        

# string = "Protiijaayiiii"
# print(fix(string))

def get_all_substrings(string):
  length = len(string)
  alist = []
  for i in xrange(length):
    for j in xrange(i,length):
      alist.append(string[i:j + 1]) 
  return alist

print(get_all_substring('abcde'))








