import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

import math
n = int(input())

mp = {}
tot = 0
for i in range(1, n+1):
    mp[i] = 0

for i in range(1, n+1):
    t = i
    for j in range(2, int(math.sqrt(i+.5))+1):
        while t % (j * j) == 0:
            t //= (j * j)
    mp[t] += 1

# printf(mp)
for k in mp.keys():
    tot += mp[k] * mp[k]

printf(tot)
