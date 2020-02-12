#Couldn't get the solver to work, it always said that the values were unsatisfiable

from z3 import *
import sys
# Read a command line argument
if len(sys.argv) > 2:
    raise SystemExit("There should be at most one argument")
elif len(sys.argv) == 2:
    try:
        N = int(sys.argv[1])
    except:
        raise SystemExit("N should be an integer")
    if N < 0:
        raise SystemExit("N should be non negative")
else:
    N = 15 #defaut value

l = []
s = []
i = 1
while(i*i < 2*N):
    s.append(i)
    i = i+1

solv = Solver()
for i in range(0,N):
    i = Int('i')
    l.append(i)
    solv.add(i > 0)
    solv.add(i < N)

for i in range(0,len(s)):
    solv.add(l[i]+l[i+1]==s[i])

Distinct(l)

result = solv.check();
if result == unsat:
    print("unsatisfiable constraints")
elif result == sat:
    print("satisfiable as:")
    m = solv.model()
    print(m[i])
    if s.check(block_model(s)) == unsat:
        print("unique solution")
    else:
        print("nonunique solution")
else:
    print('unable to solve')
