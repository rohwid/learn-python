class graph:
  def __init__(self, graph_elements=None):
    if graph_elements is None:
      graph_elements = {}
    self.graph_elements = graph_elements

  def edges(self):
    return self.findedges()
  
  # Add the new edge
  def add_edge(self, edge):
    print(f"Adding new edge {edge} with {type(edge)} type")
    
    (vrtx1, vrtx2) = tuple(edge)
    
    if vrtx1 in self.graph_elements:
      self.graph_elements[vrtx1].append(vrtx2)
    else:
      self.graph_elements[vrtx1] = [vrtx2]

  # List the edge names
  def findedges(self):
    edgename = []
    
    for vrtx in self.graph_elements:
      for nxtvrtx in self.graph_elements[vrtx]:
        if {nxtvrtx, vrtx} not in edgename:
          edgename.append({vrtx, nxtvrtx})
    
    return edgename

# Create the dictionary with graph elements
graph_elements = { 
  "a" : ["b","c"],
  "b" : ["a", "d"],
  "c" : ["a", "d"],
  "d" : ["e"],
  "e" : ["d"]
}

graph = graph(graph_elements)

print(f"Current edges: {graph.edges()}\n")

graph.add_edge({'c','e'})
graph.add_edge({'b','c'})
print()

print(f"Current edges: {graph.edges()}")