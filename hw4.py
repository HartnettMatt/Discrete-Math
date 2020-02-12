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

solv = Solver()
for i in range(0,N):
    i = Int('i')
    l.append(i)
    solv.add(i > 0)
    solv.add(i < N)

print(len(l))
Distinct(l)

s = []
for i in range(0, 2*N):
    s.append(i*i)
