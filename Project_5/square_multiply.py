#Implements the square and multiply algorithm

def squareMultiply(b, e, m):
    r = 1
    while e > 0:

        if e % 2 == 1:
            r = (r * b) % m
        b = (b * b) % m
        e >>= 1
    return r

# res = squareMultiply(275973,456789,583903)
# print("For a = 235973; e = 456789; p = 583903, we get: ", res)
#
# res = squareMultiply(984327457683,2153489582,994348472629)
# print("For a = 984327457683; e = 2153489582; p = 994348472629, we get: ", res)
