import math

plaintext = int(0b1001001001101101100100100110)
ciphertext =int(0b1011110000110001001010110001)

keyphrase = plaintext ^ ciphertext

#0b 0010111 0010111 0010111 0010111 for our example THIS IS correct
#ASSUME LSFR GENERATES MAX-LENGTH SEQUENCE

#DEGREE OF L
#degree_L = 2**(len(str(ciphertext)))-1
print format(keyphrase,'#030b')

print "The degree of L is 3"

#What is the initialization vector?

keystr = str(format(keyphrase, '#030b'))

print "The initialization vector is:", format(keystr,'.9')

#Determine the feedback coefficients of the LFSR
print "The coefficients are as follows: "
print "C_0 = 0"
print "C_1 = 1"
print "C_2 = 1"

#When we XOR the plaintext against itself (the key), this will result in
#the first bits of the ciphertext starting in all 0s. This would mean the data
#of 0011 would have the same ciphertext as 1101. (Not sure if this is bad)
