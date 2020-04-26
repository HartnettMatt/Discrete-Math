from graph import *

graph = Graph(5)
graph.add_edge(0, 1, -1)
graph.add_edge(0, 2, 4)
graph.add_edge(2, 0, 4)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 2)
graph.add_edge(1, 4, 2)
graph.add_edge(3, 2, 5)
graph.add_edge(3, 1, 1)
graph.add_edge(4, 3, -3)

graph.bellmanFord(4)
