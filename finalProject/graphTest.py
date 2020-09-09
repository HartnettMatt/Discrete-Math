from graph import *

# Build a graph of various edges to test different distance algorithms
graph = Graph(5)
graph.add_edge(0, 1, -1)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 2)
graph.add_edge(1, 4, 2)
graph.add_edge(2, 0, 4)
graph.add_edge(3, 2, 5)
graph.add_edge(3, 1, 1)
graph.add_edge(4, 3, -3)

# Expected output of last row (distance from vertex 4): 5, -2, 1, -3, 0
print("\nTesting Floyd-Warshall:")
graph.floydWarshall()
print("\nTesting Bellman-Ford at the source vertex 4:")
print("Expected output should match the last row of Floyd-Warshall")
graph.bellmanFord(4)
