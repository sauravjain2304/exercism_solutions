NODE, EDGE, ATTR = range(3)
class Node(object):
  def __init__(self, name, attrs={}):
    self.name = name
    self.attrs = attrs
  def __eq__(self, other):
    return self.name == other.name and self.attrs == other.attrs

class Edge(object):
  def __init__(self, src, dst, attrs={}):
    self.src = src
    self.dst = dst
    self.attrs = attrs

  def __eq__(self, other):
    return (self.src == other.src and
            self.dst == other.dst and
            self.attrs == other.attrs)

class Graph(object):
  def __init__(self, data=[]):
    self.nodes = []
    self.edges = []
    self.attrs = {}
    if data and len(data[0]) < 2: 
      raise TypeError('l')
    if type(data) != list: 
      raise TypeError('not list')
    for tup in data:
      if 0 > tup[0] > 2:
        raise ValueError('hi')
      elif tup[0] == NODE:
        if type(tup[2]) != dict: 
          raise ValueError('hi')
        self.nodes.append(Node(tup[1], tup[2]))
      elif tup[0] == EDGE:
        if len(tup) != 4: 
          raise  ValueError('edge')
        self.edges.append(Edge(tup[1], tup[2], tup[3]))
      elif tup[0] == ATTR:
        if len(tup) != 3: 
          raise ValueError('d')
        self.attrs[tup[1]] = tup[2]
      else:
          raise ValueError('k')            