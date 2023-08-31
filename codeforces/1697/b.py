import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

from itertools import accumulate
n, q = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
a.reverse()
s = list(accumulate(a))
s.append(0)

for _ in range(q):
    x, y = map(int, input().split())
    printf(s[x-1] - s[x-y-1])
