class Matrix:
  def __init__(self, matrix_string):
    self.a = matrix_string

  def row(self, index):
    nums = self.a.split("\n")
    return list(map(int, nums[index - 1].split()))      
    # print(f"{nums}")
    # n = int(len(nums) ** 0.5)
    # return list(map(list, zip(*[map(int, nums)] * n)))
     
  def column(self, index):
    nums = self.a.split("\n")
    col = []
    for i in nums:
      col.append(i.split()[index - 1])
    # print(" ".join(map(str, col)))
    return list(map(int, col))
