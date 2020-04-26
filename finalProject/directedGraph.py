from sys import maxsize
from collections import defaultdict

class directedGraph(object):
    def __init__(self, vertices):
        # vert_dict is the dictionary of vertices
        self.vert_dict = defaultdict(list)
        self.time = 0
        self.v = vertices

    def __iter__(self):
        return iter(self.vert_dict_values())

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

# Add directed edge to the graph, will create vertexes if they don't already exist
    def add_edge(self, frm, to):
        self.vert_dict[frm].append(to)

    def get_vertices(self):
        return self.vert_dict.keys()

# A strongly connected components based on Tarjan's algorithm:
    def SCC(self):
        disc = [-1]*self.v
        low = [-1]*self.v
        stackMember = [False]*self.v
        st = []
        for i in range(self.v):
            if disc[i] == -1:
                self.SCChelper(i, low, disc, stackMember, st)
            
# A helper function for the strongly connected components algorithm
    def SCChelper(self, u, low, disc, stackMember, st):
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        stackMember[u] = True
        st.append(u)

        for v in self.vert_dict[u]:
            if disc[v] == -1:
                self.SCChelper(v, low, disc, stackMember, st)
                low[u] = min(low[u], low[v])
            elif stackMember[v] == True:
                low[u] = min(low[u], disc[v])
        w = -1
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                print(w, end = " ")
                stackMember[u] = False
            print("\n")
