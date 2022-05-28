import sys;input=lambda:sys.stdin.readline().strip("\r\n")
import platform
LOCAL = (platform.uname().node == 'AMO')
# print(LOCAL)
def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

import math

n, a, b = map(int, input().split())
c = a * b // math.gcd(a, b)

tot = (1 + n) * n // 2

x = n // a
y = n // b
z = n // c

# printf([x, y, z])

tot -= a * (1 + x) * x // 2
tot -= b * (1 + y) * y // 2
tot += c * (1 + z) * z // 2

printf(tot)
