from sys import maxsize
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # Array to track vertices
        self.graph = []

    def add_edge(self, frm, to, weight):
        self.graph.append([frm,to,weight])

    def bellmanFord(self,src):
        print("Running Bellman Ford algorithm:")
        dist = [maxsize]*self.V
        dist[src] = 0

        for k in range(self.V -1):
            for frm, to, weight in self.graph:
                distance = dist[frm] + weight
                if dist[frm] != maxsize and distance < dist[to]:
                    dist[to] = distance

        for frm, to, weight in self.graph:
            distance = dist[frm] + weight
            if dist[frm] != maxsize and distance < dist[to]:
                print("Negative weight cycle")
                return

        print("Distance from source:")
        for i in range(self.V):
            if dist[i] != maxsize:
                print(str(i) + "\t" + str(dist[i]))
            else:
                print(str(i) + "\tNo Path from source")


    def printGraph(self):
        for i in self.graph:
            print(str(i))

    def floydWarshall(self):
        # Build a matrix to store the graph with maxsize weights
        # matrixGraph[start vertex][end vertex][edge weight]
        matrixGraph = [[maxsize for i in range(self.V)] for j in range(self.V)]

        for i in self.graph:
            frm = i[0]
            to = i[1]
            weight = i[2]
            matrixGraph[frm][frm] = 0
            matrixGraph[frm][to] = weight

        dist = matrixGraph
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        for i in dist:
            print(i)
