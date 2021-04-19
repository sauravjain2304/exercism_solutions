from __future__ import division
class Rational:
  def __init__(self, numer, denom):
    self.numer = numer
    self.denom = denom
    self.reduct()
      
  def reduct(self):
    if self.numer == 0:
      self.denom = 1
      return
    for i in range(min(abs(self.numer), abs(self.denom)),0,-1):
      if self.numer % i == 0 and self.denom % i == 0:
        self.numer = self.numer // i
        self.denom = self.denom // i
        if self.denom < 0:
          self.numer = -self.numer
          self.denom = -self.denom
        return
        
  def __eq__(self, other):
    return self.numer == other.numer and self.denom == other.denom

  def __repr__(self):
    return '{}/{}'.format(self.numer, self.denom)

  def __add__(self, other):
    return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

  def __sub__(self, other):
    return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

  def __mul__(self, other):
    return Rational(self.numer * other.numer, self.denom * other.denom)

  def __truediv__(self, other):
    if self.denom * other.numer == 0:
      raise ValueError("division by zero")
    return Rational(self.numer * other.denom, self.denom * other.numer)

  def __abs__(self):
    return Rational(abs(self.numer), abs(self.denom))

  def __pow__(self, power):
    if power <0:
        return Rational(self.denom ** abs(power), self.numer ** abs(power))            
    return Rational(self.numer ** power, self.denom ** power)

  def __rpow__(self, base):
    return base ** (self.numer/self.denom)