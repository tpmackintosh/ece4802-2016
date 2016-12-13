from collections import deque

row0 = [0,1,2,3,4,5,6,7]

for j in range(1,7):
    for i in range(1,7):
        row0[j] = j * row0[j]
        if row0[j] > 7:
            row0[j] = row0[j] ^ j

        print row0
