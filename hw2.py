# The solution found from z3 is that Alex has to be a knave, and no conclusions can be drawn about the mother
from z3 import *
s = Solver()
a = Bool('a')
m = Bool('m')

# Build the model with the proper initial constraints
s.add(Implies(a, m == And(a != m)))

result = s.check()

# Check satisfiablity and if satisfiable, find all possible solutions to the model
if result == unsat:
    print("unsatisfiable constraints")
elif result == sat:
    while s.check() == sat:
        j = s.model()
        print(', '.join([str(x) + ' = ' + str(j[x]) for x in [a, m]]))
        s.add(Or(a != s.model()[a], m != s.model()[m]))
else:
    print('unable to solve')
