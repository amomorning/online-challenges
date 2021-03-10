import math
import sys
def is_prime(val):
    if(val == 0): return False
    if(val == 1): return False
    if(val == 2): return True
    for i in range(2, int(math.sqrt(val))+1):
        if(val % i == 0):
            return False
    return True

def trans(val, rad):
    ret = ''
    while(val > 0):
        ret += str(val % rad)
        val = val // rad
    return ret


for e in iter(input, '-1'):
    try:
        n, d = map(int, e.split())

        if (is_prime(n) and is_prime(int(trans(n, d), d))):
            print('Yes')
        else: print('No')
    except ValueError:
        break
