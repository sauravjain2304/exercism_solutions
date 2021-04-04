class Queen:
  def __init__(self, row, column):
    if not -1 < row < 8:
      raise ValueError("error")
    if not -1 < column < 8:
      raise ValueError("error")
    self.row = row
    self.column = column

  def can_attack(self, another_queen):
    if self.row == another_queen.row and self.column == another_queen.column:
      raise ValueError("error")
    if self.row == another_queen.row:
        return True
    if self.column == another_queen.column:
        return True
    grad = (self.row - another_queen.row) / (self.column  - another_queen.column)
    if abs(grad) == 1:
        return True
    return False
obj = Queen(2, 4)
print(obj.can_attack(Queen(6, 6)))