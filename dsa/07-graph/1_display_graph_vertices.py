class Graph:
  def __init__(self, gdict=None):
    if gdict is None: gdict = []
    self.gdict = gdict
      
  # Get the keys of the dictionary
  def get_vertices(self):
    print(list(self.gdict.keys()))

# Create the dictionary with graph elements
graph_elements = { 
  "a" : ["b","c"],
  "b" : ["a", "d"],
  "c" : ["a", "d"],
  "d" : ["e"],
  "e" : ["d"]
}

graph = Graph(graph_elements)
graph.get_vertices()