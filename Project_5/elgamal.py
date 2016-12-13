from square_multiply import squareMultiply

def getKey_M(a, d, i, p):
    beta = squareMultiply(a, d, p)
    k_m = squareMultiply(beta, i, p)

    return k_m

a = 2
p = 467

arr_d = [105, 105, 300, 300]
arr_i = [213, 123, 45, 47]

for i in range(4):
    temp = getKey_M(a, arr_d[i], arr_i[i], p)
    print "Number of ciphertexts for ", i + 1, ":", temp


x1 = 27 #message, y = 49
c1 = 389
c2 = 299
p = 467
y = 0

#Find session key y
for i in range(467):
    c = x1 * i%p
    if c == 389:
        print i
        y = i
        break

print c2*(y**-1)%p
