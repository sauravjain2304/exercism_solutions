class PhoneNumber:
  def __init__(self, number):
    self.number = ''.join(s for s in number if s.isdigit())
        
    if self.number[0] == "1" and len(self.number) > 10:
      self.number = self.number[1:]

    if len(self.number) != 10:
      raise ValueError("error")

    if int(self.number[0]) <= 1:
      raise ValueError("error")

    if int(self.number[3]) <= 1:
      raise ValueError("error")

    
    self.area_code = self.number[:3]
    self.exchange_code = self.number[3:6]
    self.subscriber_number = self.number[6:]

  def pretty(self):
    return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
