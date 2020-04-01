#Loop invarient: gdc(x,y) = gcd(a,b) && 0 <= y <= x
def euclid(a: int, b: int) -> int:
    x,y = abs(a), abs(b)
    while y != 0:
        print("x = " + str(x) + " y = " + str(y))
        x,y = y, x%y
    return x

euclid(420, 69)
