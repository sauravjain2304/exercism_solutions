def square_of_sum(number):
  n = (number * (number + 1)) / 2
  n = n * n
  return n
def sum_of_squares(number):
  n = (number * (number + 1) * (2 * number + 1)) / 6
  return n
def difference_of_squares(number):
  return square_of_sum(number) - sum_of_squares(number)  