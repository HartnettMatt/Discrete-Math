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

    def add_adjacent(self, adjacent):
        self.adjacent[adjacent] = 1

    def get_adjacent(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id


class directedGraph(object):
    def __init__(self):
        # vert_dict is the dictionary of vertices
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict_values())

    def add_vertex(self, name):
        if name not in self.vert_dict:
            self.num_vertices += 1
            new_vertex = Vertex(name)
            self.vert_dict[name] = new_vertex
            return new_vertex
        else:
            print("Name: " + name + " already used")

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

# Add directed edge to the graph, will create vertexes if they don't already exist
    def add_edge(self, frm, to):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_adjacent(self.vert_dict[to])

    def get_vertices(self):
        return self.vert_dict.keys()

# Set all distances to zero and all vertexes to unvisited
    def reset_graph(self):
        for k in self.vert_dict:
            self.vert_dict[k].distance = 0
            self.vert_dict[k].visited = False

# Set distance of all vertices to maximum
    def set_graph(self):
        for k in self.vert_dict:
            self.vert_dict[k].distance = maxsize

    def fillUp(self, v, stack):
        v.visited = True
        for i in v.adjacent:
            if i.visited == False:
                self.fillUp(i, stack)
        stack.append(v)

    def reverse(self):
        r = directedGraph()
        for i in self.vert_dict:
            for j in self.vert_dict[i].adjacent:
                r.add_edge(j.get_id(),i)
        return r

    def DFSUtil(self, v):
        v.visited = True
        print(str(v.get_id()) + ",", end = "")
        for i in v.adjacent:
            if i.visited == False:
                self.DFSUtil(i)

    def printSCC(self):
        stack = []
        self.reset_graph()
        for i in self.vert_dict:
            if self.vert_dict[i].visited == False:
                self.fillUp(self.vert_dict[i], stack)

        reversed = self.reverse()
        self.reset_graph()
        print("The strongly connected components in this graph are:")
        while stack:
            i = stack.pop()
            if i.visited == False:
                reversed.DFSUtil(i)
                print("\n")

    def SCC1(self):
        for i in self.vert_dict:
            self.vert_dict[i].distance = -1
