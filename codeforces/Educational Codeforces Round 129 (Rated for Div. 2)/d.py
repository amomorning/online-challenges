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

from collections import deque

def getdigits(x):
    return list(map(int, list(str(x))))


def solve():
    n, x = map(int, input().split())

    target = 10**(n-1)

    q = deque()
    q.append((x, 0))
    vis = {}

    if x >= target*10:
        printf(-1)
        return 


    while q:
        # printf(q)
        u, step = q.popleft()
        
        ds = getdigits(u)
        
        for d in range(9, 1, -1):
            if d in ds:
                if d*u >= target:
                    printf(step+1)
                    return
                
                if d*u not in vis:
                    vis[d*u] = 1
                    q.append((d*u, step+1))
    
    printf(-1)
    return

solve()
