def latest(scores):
  return scores[-1]


def personal_best(scores):
  return max(scores)
  


def personal_top_three(scores):
  scores.sort()
  return scores[::-1][0:3]
  #return scores[-3:]
   

  
# scores = [2, 4, 54, 36, 100, 9]
# latest(scores)
# print(latest(scores))
# personal_best(scores)
# print(personal_best(scores))
# personal_top_three(scores)
# print(personal_top_three(scores))
