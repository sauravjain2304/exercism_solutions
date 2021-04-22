class Point:
  def __init__(self, x, y):
    self.x = None
    self.y = None

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y


class WordSearch:
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
  def __init__(self, puzzle):
    self.puzzle = puzzle

  def search(self, word):
    for y in range(len(self.puzzle)):
      for x in range((len(self.puzzle[0]))):
        if self.puzzle[y][x] != word[0]:
          continue
        else:
          for d in self.directions:
            chunk = self.puzzle[y][x]
            x2 = x
            y2 = y
            while True:
              try:
                if chunk == word:
                  return Point(x, y), Point(x2, y2)
                x2 += d[0]
                y2 += d[1]
                chunk += self.puzzle[y2][x2]
              except:
                break
  