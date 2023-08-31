import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

from collections import deque

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))

    cur = 0
    d = []
    for i in range(n):
        if s[i] > cur:
            cur = s[i]
        d.append(f[i] - cur)
        cur = f[i]
    
    printf(d)
        



