class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.visited = False
        self.distance = 0

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbour(self, neighbour, weight = 0):
        self.adjacent[neighbour] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbour):
        return self.adjacent[neighbour]

class Graph(object):
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict_values())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, weight = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbour(self.vert_dict[to], weight)
        self.vert_dict[to].add_neighbour(self.vert_dict[frm], weight)

    def get_vertices(self):
        return self.vert_dict.keys()

    def dijkstra(self, frm, to):
        if to not in self.vert_dict:
            print("error: starting point not found")
            return None
        if frm not in self.vert_dict:
            print("error: destination not found")
            return None
        self.vert_dict[frm].visited = True
        self.vert_dict[frm].distance = 0
        solvedList = [self.vert_dict[frm]]
        temp = Vertex('temp')
        temp = self.vert_dict[frm]
        solvedV = Vertex('solved')
        while self.vert_dict[to].visited != True:
            minDist = 2147483647
            for x in range(len(solvedList)):
                temp = solvedList[x]
                for i in temp.adjacent:
                    if i.visited == False:
                        dist = temp.distance + temp.get_weight(i)
                        if dist < minDist:
                            minDist = dist
                            solvedV = i
            solvedV.distance = minDist
            solvedV.visited = True
            solvedList.append(solvedV)
        return self.vert_dict[to].distance

graph = Graph()

graph.add_vertex('a')
graph.add_vertex('b')
graph.add_edge('a','b',9)
graph.get_vertices
print(graph.get_vertices())
print(graph.get_vertex('a'))
print(graph.dijkstra('a','b'))
