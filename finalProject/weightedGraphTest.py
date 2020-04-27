# Graph Test Code:
from weightedGraph import *

graph = weightedGraph()

# Build a graph of various connections with various weights for testing purposes
graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')
graph.add_vertex('d')
graph.add_vertex('e')
graph.add_vertex('f')
graph.add_vertex('g')

graph.add_edge('a','b',2)
graph.add_edge('a','c',1)
graph.add_edge('a','d',3)
graph.add_edge('b','d',1)
graph.add_edge('b','e',7)
graph.add_edge('c','d',1)
graph.add_edge('d','f',1)
graph.add_edge('d','e',10)
graph.add_edge('f','g',1)
graph.add_edge('g','e',4)

# Testing of a few graph functions:
print("\nTesting functions from graph:")
print(graph.get_vertices())
print(graph.get_vertex('a'))
graph.add_edge('f','a',-1)

# Testing DijkstraAlgorithm:
print("\nTesting single connection: \nExpected output = 2")
print("Dijkstra Output = " + str(graph.dijkstra('a','b')))

print("\nTesting 3 possible routes: \nExpected output = 2")
print("Dijkstra Output = " + str(graph.dijkstra('a','d')))

print("\nTesting 7 possible routes: \nExpected output = 8")
print("Dijkstra Output = " + str(graph.dijkstra('a','e')))
