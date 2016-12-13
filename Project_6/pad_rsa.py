import random
import math
from Crypto.Util import number

def pad(M,N):
    """
    The function that return padded message with size |N| -1
    first generate random r and return r||M
    The size of r is determined by size of M and N
    """
    magN = 1024
    l = 256
    r = random.getrandbits(magN - l - 1)
    r << (magN + 1)
    res = r | M
    return res

def paddedRSAEnc(m,e,n):
    """
    The function that return m^e (mod n)
    We know that m = r||M
    """
    enc = pow(m,e,n)
    return enc

def paddedRSADec(c,d,n,l):
    """
    The function that return last l bit of c^d (mod n)
    """
    res = bin(pow(c,d,n))[:l+2]
    return res


def RSAGen():
    """
    The function to create prime numbers p and q
    calculate N = p*q and phi = (p-1)*(q-1) and
    also public key <N,e> and private key <p,q,d>
    """

    q = number.getPrime(512)
    p = number.getPrime(512)

    n = p*q
    phi = (p-1)*(q-1)
    print(int(math.log(phi, 2)) + 1)
    print(int(math.log(n, 2)) + 1)
    e = 2**16+1
    if number.GCD(e,phi) != 1: print("Error: GCD(e,phi) != 1.")
    d = number.inverse(e,phi)

    return e,d,n

def RSATest():
    """
    create random message and encrypt the message
    to get ciphertext and decrypt the ciphertext to
    getback to plaintext.
    """
    M = random.randint(0,2**256-1)
    (e,d,N) = RSAGen()
    padded_message = pad(M,N)

    c = paddedRSAEnc(M,e,N)
    l = 256
    M1 = paddedRSADec(c,d,N,l)
    print("M1 = ", M1)
    print("M =  ", bin(M))
    if M == int(M1,2):
        print("Correct")
    else:
        print("Wrong ...")


RSATest()
