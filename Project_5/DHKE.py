import random
from square_multiply import squareMultiply
import hashlib

def isPrime(p):
    if(p==2): return True
    if(not(p&1)): return False
    return squareMultiply(2,p-1,p)==1

def rand_prime():
    while True:
        p = random.getrandbits(1023)
        q = int(p)
        if isPrime(q) == True:
            return q

def gen_Key(k_A):
    hashkey = hashlib.sha224(hex(k_A)[2:-1].decode('hex'))
    return hashkey

def checkEqual(a,b):
    if a == b:
        print "k_A = k_B"
    else:
        print "Keys not equal"

random.seed(12345)

p = rand_prime()
p_safe = int("""
136493091133649836164289363338682002944029379014077033130604363922256595
037775025761962540974136000872788770954019530710825866837156972143526820\
463536654299014569407235702375016873961943932744861043443226534544334946\
757053788912168896006231429590913701778250440452439749688803485407941150\
333770430825062090319""".replace("\n",""))

a = random.randrange(1,p_safe-2)
b = random.randrange(1,p_safe-2)
g = random.randrange(1,p_safe-1)
A = squareMultiply(g,a,p_safe)
B = squareMultiply(g,b,p_safe)

print "a= ", a,"\n\nb= ",b,"\n\np= ",p, "\n\np_safe= ", p_safe, "\n\ng= ",g, "\n"

k_A = squareMultiply(A,b,p_safe)
k_B = squareMultiply(B,a,p_safe)
checkEqual(k_A,k_B)

print "Hashed key: ",gen_Key(k_A).hexdigest()
