class graph:
  def __init__(self, graph_elements=None):
    if graph_elements is None:
      graph_elements = {}
      
    self.graph_elements = graph_elements
    self.edges_name = []
    
  # Find the distinct list of edges
  def set_edges(self):
    for vertex in self.graph_elements:
      print(f"Working in Vertex: {vertex.upper()}")
      print(f"---------------------")
      
      for element in self.graph_elements[vertex]:
        if {element, vertex} not in self.edges_name: # matching set
          self.edges_name.append({vertex, element})
          print(f"Edge added: {self.edges_name[-1]}")
      
      print(f"Current edges: {self.edges_name}\n")
    
    print(f"Done.\n\n")
    
  def get_edges(self):
    return self.edges_name
  
  def get_vertex_edges(self, vertex):
    vertex_edges = []
    
    if vertex not in self.graph_elements:
      return None
    
    for edge in self.edges_name: # matching set
      if vertex in edge:
        for get_vertex in edge:
          if get_vertex != vertex: # matching set
            vertex_edges.append(get_vertex)  
            
    return vertex_edges

# Create the dictionary with graph elements
graph_elements = { 
  "a" : ["b","c"],
  "b" : ["a", "d"],
  "c" : ["a", "d"],
  "d" : ["e"],
  "e" : ["d"]
}

graph = graph(graph_elements)
graph.set_edges()

print(f"List of all edges: {graph.get_edges()}\n")

conn_vertex = 'b'
print(f"Vetex {conn_vertex.upper()} connect with {graph.get_vertex_edges(conn_vertex)} vertices.")