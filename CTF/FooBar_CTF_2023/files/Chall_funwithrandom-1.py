import random
import os
from Flag import flag

random.seed(os.urandom(8))
mt = list(random.getstate()[1])
N= 624
M = 397
MATRIX_A = 0x83a2b0c3
UPPER_MASK =  0x80000000  
LOWER_MASK =  0x7fffffff

TemperingMaskB = 0x3f5663d0
TemperingMaskC = 0x56e90000

mag01 = [0, MATRIX_A]
mt_index = 624
def rand_gen():
    global mt_index
    if mt_index>=N:
        for kk in range(N-M):
            y = (mt[kk]&UPPER_MASK)|(mt[kk+1]&LOWER_MASK)
            mt[kk] = mt[kk+M] ^ (y >> 1) ^ mag01[y & 0x1]

        for kk in range(N-M, N-1):
            y = (mt[kk]&UPPER_MASK)|(mt[kk+1]&LOWER_MASK)
            mt[kk] = mt[kk+(M-N)] ^ (y >> 1) ^ mag01[y & 0x1]

        y = (mt[N-1]&UPPER_MASK)|(mt[0]&LOWER_MASK)
        mt[N-1] = mt[M-1] ^ (y >> 1) ^ mag01[y & 0x1]
        mt_index = 0

    y = mt[mt_index]
    y ^= (y >> 43)
    y ^= (y << 12) & TemperingMaskB
    y ^= (y << 67) & TemperingMaskC
    y ^= (y >> 69)
    mt_index+=1

    return y

output = []
for _ in range(624):
    output.append(rand_gen())

Banner = "Thou shall guess the next 5 random numbers or burn in the eternal fire of RPNG Generator\n"
print(Banner)
print(output)
print("\n")
for i in range(5):
    response= int(input(f"Number {i+1}: "))
    if response!= rand_gen():
        print("Incorrect!!")
        exit(1)

print(flag)

