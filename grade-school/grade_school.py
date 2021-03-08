class School:
  def __init__(self):
    self.student = {}
    
  def add_student(self, name, grade):
    if grade in self.student:
      self.student[grade].append(name)
    else:  
      self.student.update({grade: [name]})
    
  def roster(self):
    b = []
    for i in sorted(self.student.keys()):
      b.append(sorted(self.student[i]))
    c = sum(b, [])
    return c  
       

  def grade(self, grade_number):
    return sorted(self.student.get(grade_number, []))