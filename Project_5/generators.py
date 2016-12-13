#This program starts by determining the generators of the non-zero integers
#in the group Zp where p is 4969
import math
from square_multiply import squareMultiply

gen_count = 0

for i in range(1,4969):
    temp = math.gcd(i,4968)
    if temp == 1:
        gen_count += 1

print(gen_count) #1584

#An integer is a generator if integer ^ 4968 = 1 mod 4969

for a in range(1000,5000):
    temp = squareMultiply(a,4968,4968)
    if temp == 1:
        print(a)
        break
