class Garden:
  def __init__(self, diagram, students=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
                                           'Harriet','Ileana', 'Joseph', 'Kincaid', 'Larry' ] ):
                                           
    self.diagram = diagram.split("\n")
    self.students = students

  def plants(self, name):
    dict_plants = {"V":'Violets', "R":'Radishes', "C":'Clover', "G":'Grass' }
    self.students.sort()
    name_position = self.students.index(name) * 2

    res = []
    for i in self.diagram:
      res.append(dict_plants[i[name_position]])
      next_position = name_position + 1
      res.append(dict_plants[i[next_position]])
    return res
