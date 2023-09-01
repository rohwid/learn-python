class graph:
  def __init__(self, graph_elements=None):
    if graph_elements is None:
      graph_elements = {}
    self.graph_elements = graph_elements
   
  def get_vertices(self):
    return list(self.graph_elements.keys())
  
  # Add the vertex as a key
  def add_vertex(self, vrtx):
    if vrtx not in self.graph_elements:
      self.graph_elements[vrtx] = []

# Create the dictionary with graph elements
graph_elements = { 
  "a" : ["b","c"],
  "b" : ["a", "d"],
  "c" : ["a", "d"],
  "d" : ["e"],
  "e" : ["d"]
}

graph = graph(graph_elements)
graph.add_vertex("f")

print(graph.get_vertices())