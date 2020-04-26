from sys import maxsize
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # Array to track vertices
        self.graph = []
        # Array to track distance from source
        self.dist = []

    def add_edge(self, frm, to, weight):
        self.graph.append([frm,to,weight])

    def bellmanFord(self,src):
        print("Running Bellman Ford algorithm:")
        self.dist = [maxsize]*self.V
        self.dist[src] = 0

        for k in range(self.V -1):
            for frm, to, weight in self.graph:
                distance = self.dist[frm] + weight
                if self.dist[frm] != maxsize and distance < self.dist[to]:
                    self.dist[to] = distance

        for frm, to, weight in self.graph:
            distance = self.dist[frm] + weight
            if self.dist[frm] != maxsize and distance < self.dist[to]:
                print("Negative weight cycle")
                return

        print("Distance from source:")
        for i in range(self.V):
            if self.dist[i] != maxsize:
                print(str(i) + "\t" + str(self.dist[i]))
            else:
                print(str(i) + "\tNo Path from source")
