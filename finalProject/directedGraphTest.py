from directedGraph import *

graph = directedGraph()

graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')
graph.add_vertex('d')
graph.add_vertex('e')
graph.add_vertex('f')
graph.add_vertex('g')

graph.add_edge('a','b')
graph.add_edge('b','d')
graph.add_edge('d','c')
graph.add_edge('c','a')

graph.add_edge('d','f')
graph.add_edge('f','g')
graph.add_edge('g','e')
graph.add_edge('e','f')

graph.SCC()
