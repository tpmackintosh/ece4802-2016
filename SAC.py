
def S2(x): #Implementation of S Box 2, returns value from row

    row0 = [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10]
    row1 = [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5]
    row2 = [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15]
    row3 = [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    s2 = 0
    x = '0b'+bin(x^2**6)[3:]
    if x[2] == "0":
        if x[7] == "0":
            y = int(x[3:7],2)
            s2 = row0[y]
        if x[7] == "1":
            y = int(x[3:7],2)
            s2 = row1[y]

    if x[2] == "1":
        if x[7] == "0":
            y = int(x[3:7],2)
            s2 = row2[y]
        if x[7] == "1":
            y = int(x[3:7],2)
            s2 = row3[y]


    return s2;


def SAC(x):
    Sum = 0
    output = [0,0,0,0,0,0]

    for i in range(0,6):
        output[i] = S2(x) ^ S2(x^2**i)
    return output;

sum0 = 0
sum1 = 0
sum2 = 0
sum3 = 0

for j in range(2**6):
    bit0 = 0; bit1 = 0; bit2 = 0; bit3 = 0
    arr = SAC(j)

    for i in range (0,6):
        bit0 += int(bin(arr[i]^(2**4))[6])
        bit1 += int(bin(arr[i]^(2**4))[5])
        bit2 += int(bin(arr[i]^(2**4))[4])
        bit3 += int(bin(arr[i]^(2**4))[3])
    sum0 += (bit0 % 2)
    sum1 += (bit1 % 2)
    sum2 += (bit2 % 2)
    sum3 += (bit3 % 2)

print sum0, sum1, sum2, sum3
