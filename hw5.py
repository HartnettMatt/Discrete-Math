# Z3 successfully prints out valid when the script is run
from z3 import *
x = Int('x')
y = Int('y')
z = Int('z')
A1 = ForAll([x], Exists([y],And(x>y,ForAll([z],Or(x >= z, z >= y)))))
s = Solver()
s.add(Not(A1))
result = s.check()
if result == unsat:
    print("Valid")
elif result == sat:
    print("Not valid")
else:
    print("very not valid")
