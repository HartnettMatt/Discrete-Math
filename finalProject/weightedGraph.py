from sys import maxsize
class Vertex:
    def __init__(self, name):
        self.id = name
        self.adjacent = {}
        self.visited = False
        # Distance is a temporary to keep track in Dijkstra
        self.distance = 0

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_adjacent(self, adjacent, weight = 0):
        self.adjacent[adjacent] = weight

    def get_adjacent(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, adjacent):
        return self.adjacent[adjacent]

class Graph(object):
    def __init__(self):
        # vert_dict is the dictionary of vertices
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict_values())

    def add_vertex(self, name):
        self.num_vertices += 1
        new_vertex = Vertex(name)
        self.vert_dict[name] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

# Add weighted edge to the graph, will create vertexes if they don't already exist
    def add_edge(self, frm, to, weight = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_adjacent(self.vert_dict[to], weight)
        self.vert_dict[to].add_adjacent(self.vert_dict[frm], weight)

    def get_vertices(self):
        return self.vert_dict.keys()

# Set all distances to zero and all vertexes to unvisited
    def reset_graph(self):
        for k in self.vert_dict:
            self.vert_dict[k].distance = 0
            self.vert_dict[k].visited = False

# Find the fastest path from two points in a weighted graph
    def dijkstra(self, frm, to):
        # Make sure that both points are in the graph
        if to not in self.vert_dict:
            print("error: destination point not found")
            return -1
        if frm not in self.vert_dict:
            print("error: starting point not found")
            return -1

        # Intialize starting values:
        self.vert_dict[frm].visited = True
        self.vert_dict[frm].distance = 0
        solvedList = []
        solvedList.append(self.vert_dict[frm])

        # Temp keeps track of which vertex is being tested
        temp = self.vert_dict[frm]

        # solvedV keeps track of which vertex is closest for that iteration
        solvedV = Vertex('solved')

        # Loop until the destination is reached
        while self.vert_dict[to].visited != True:
            minDist = maxsize
            for x in solvedList:
                temp = x
                for i in temp.adjacent:
                    if i.visited == False:
                        dist = temp.distance + temp.get_weight(i)
                        if dist < minDist:
                            minDist = dist
                            solvedV = i
            solvedV.distance = minDist
            solvedV.visited = True
            solvedList.append(solvedV)

        # Store actual distance, reset the graph, and return:
        distance = self.vert_dict[to].distance
        self.reset_graph()
        return distance

# Set distance of all vertices to maximum
    def set_graph(self):
        for k in self.vert_dict:
            self.vert_dict[k].distance = maxsize

# Find the distance from source node to destination disregarding weight
    def breadthFirst(self, frm, to):
        self.set_graph()
        self.vert_dict[frm].distance = 0
        self.vert_dict[frm].visited = True
        q = []
        q.append(self.vert_dict[frm])
        while q:
            temp = q.pop()
            for i in temp.adjacent:
                dist = temp.distance + temp.get_weight(i)
                if dist < i.distance:
                    i.distance = dist
                if i.visited == False:
                    q.append(i)
                    i.visited = True
        return self.vert_dict[to].distance
