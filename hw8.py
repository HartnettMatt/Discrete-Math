# I was unable to complete this assignment, because I could not add the necessary constraints into z3
from z3 import*
def set_cover(Ca):
    x = []
    # for i in range(0,Ca.max()):
    #     x.append(Bool('x'))
    # print(x)
    opt = Optimize()
    m = max(Ca[0]);
    for i in range(0,len(Ca)):
        for j in range(1, len(Ca[i])):
            if (max(Ca[i]) > m):
                m = max(Ca[i])

    for k in range(0, m):
        x.append(Bool('x'))

    print(len(x))
    for l in range(0, len(Ca)):
        opt.add(And(Ca[l]))
    opt.add()
    opt.minimize(Sum([If(v, 1, 0) for v in x]))

if __name__ == '__main__':
    Ca = [{0,10}, {0,1,4}, {1,2,4,5,6,7}, {0,1,3,5,9}, {0,3}, {2,6,8,11}, {2,7,8,10}, {3,9}]
    print(set_cover(Ca))
