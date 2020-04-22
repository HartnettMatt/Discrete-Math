# Could not get functioon, never could make it so that the solver would block previous models
from z3 import Solver, Int, And, Or, ArithRef, BoolRef, sat, Not

from typing import Sequence, Collection

Graph = Sequence[Collection[Int]]
VarList = Sequence[ArithRef] #Sequence of Z3 integer variables
Graph = ({1,2}, {0,3}, {0,3}, {1,2})

def ColoringCounter(G: Graph, k:int):
    n = len(G) #Number of vertices
    c = 0
    s = Solver()
    v = [Int('v%i'%i) for i in range(n)]
    s.add([And(x >= 0, x < k) for x in v])
    for i in range(n):
        s.add([v[i] != v[j] for j in G[i]])
    while c <= 4 and s.check() == sat:
        c += 1
        m = s.model()
        VarList = m
        print(str([m[x] for x in v]))
        print(str(v))
        for i in range(n):
            s.add([v[i] != Int('m[i]')])

    return c

print(str(ColoringCounter(Graph, 4)))
