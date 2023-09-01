class Graph:
  def __init__(self, graph_elements=None):
    if graph_elements is None: graph_elements = []
    self.graph_elements = graph_elements
      
  # Get the keys of the dictionary
  def get_vertices(self):
    print(list(self.graph_elements.keys()))

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