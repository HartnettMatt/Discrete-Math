from sympy import isprime
from mpmath import mp

decimalPlaces = 100
with mp.workdps(decimalPlaces):
        estring = str(mp.e).replace('.','')

# print(estring)
# Number of digits that have to be a prime number
primeDigits = 12
# Loop to check for a prime
for i in range(decimalPlaces-primeDigits):
    subInt = int(estring[i:i+primeDigits])
    if(isprime(subInt)):
        print(subInt)
        break
