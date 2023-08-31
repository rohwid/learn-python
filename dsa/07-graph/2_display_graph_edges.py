class graph:
  def __init__(self, graph_dict=None):
    if graph_dict is None:
      graph_dict = {}
      
    self.graph_dict = graph_dict

  # Find the distinct list of edges
  def find_edges(self):
    edge_name = []
      
    for vertex in self.graph_dict:
      print(f"Working in vertex : {vertex.upper()}")
      for conn_vertex in self.graph_dict[vertex]:
        if {conn_vertex, vertex} not in edge_name:
          edge_name.append({vertex, conn_vertex})
          print(f"Edge added        : {edge_name[-1]}")
      print(f"Current edges     : {edge_name}\n")

# Create the dictionary with graph elements
graph_elements = { 
  "a" : ["b","c"],
  "b" : ["a", "d"],
  "c" : ["a", "d"],
  "d" : ["e"],
  "e" : ["d"]
}

graph = graph(graph_elements)
graph.find_edges()