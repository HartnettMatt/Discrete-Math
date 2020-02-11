# The solution found from z3 is that both V and W have to be guilty
from z3 import *
s = Solver()
a = Bool('a')
b = Bool('b')
c = Bool('c')
d = Bool('d')
e = Bool('e')
f = Bool('f')
g = Bool('g')
h = Bool('h')
v = Bool('v')
w = Bool('w')

# A method to test the uniqueness of the solution found
def  block_model(s):
    m = s.model ()
    return  Or([v != m[v] for v in [v, w]])

# Build the model with the proper initial constraints
s.add(a == a)
s.add(c == Not(a))
s.add(d == Not(b))
s.add(e == And(c, d))
s.add(f == Not(And(Not(a), Not(b))))
s.add(g == Or(And(e, f), And(Not(e),Not(f))))
s.add(h == And(Or(And(e, f), And(Not(e),Not(f)))), And(Not(v),Not(w)))
result = s.check()

# Check satisfiablity and if satisfiable, test the uniqueness of the solution
if result == unsat:
    print("unsatisfiable constraints")
elif result == sat:
    print("satisfiable as:")
    m = s.model()
    print(', '.join([str(v) + ' = ' + str(m[v]) for v in [v, w]]))
    if s.check(block_model(s)) == unsat:
        print("unique solution")
    else:
        print("nonunique solution")
else:
    print('unable to solve')
