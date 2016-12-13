#CT observed J5A0EDJ2B
from collections import deque
#from bitarray import bitarray

init_vec = [1,1,1,1,1,1]
ciphertext = ['J',5,'A',0,'E','D','J',2,'B']
key =[]

cipherbin = []

#GENERATES KEY
key.insert(0,'1')
for j in range(0,44):
    a = int(init_vec[4]) ^ int(init_vec[5])
    init_vec.insert(0,a)
    init_vec.pop()

    key.append(str(init_vec[5]))



#GENERATE BITSTREAM FROM CIPHERTEXT
for j in range(0,9):
    if type(ciphertext[j]) == str:
        cipherbin.append(str(format((ord(ciphertext[j])-ord('A')),'05b')))
    else:
        cipherbin.append(str(format((ord(str(ciphertext[j])) - 22),'05b')))

#print "The cipher " +'{}{}{}{}{}{}{}{}{}'.format(*cipherbin)

#XOR THE CIPHER AND THE KEY

a = "0b"+''.join(key)
b = "0b"+''.join(cipherbin)



plainbin = str(bin(int(a.strip(""),2) ^ int(b.strip(""),2)))


print "Key       0b"+'{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(*key)
print "Cipher    0b"+'{}{}{}{}{}{}{}{}{}'.format(*cipherbin)
print "Plaintext " +plainbin


u0 = chr(int(("0b"+''.join(plainbin[2:7])).strip(""),2)+ord("A"))
u1 = chr(int(("0b"+''.join(plainbin[7:12])).strip(""),2) + 65)
u2 = chr(int(("0b"+''.join(plainbin[12:17])).strip(""),2)+ord("A"))
u3 = chr(int(("0b"+''.join(plainbin[17:22])).strip(""),2) + 65)
u4 = chr(int(("0b"+''.join(plainbin[22:27])).strip(""),2)+ord("A"))
u5 = chr(int(("0b"+''.join(plainbin[27:32])).strip(""),2)+ord("A"))
u6 = chr(int(("0b"+''.join(plainbin[32:37])).strip(""),2)+ord("A"))
u7 = chr(int(("0b"+''.join(plainbin[37:42])).strip(""),2) + 65)
u8 = chr(int(("0b"+''.join(plainbin[42:47])).strip(""),2)+ord("A"))

print u0,u1,u2,u3,u4,u5,u6,u7,u8
