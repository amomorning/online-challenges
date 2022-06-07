import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

def find_period(cycle):
    raw = ''.join(cycle)
    for i in range(n):
        cycle.rotate()
        if ''.join(cycle) == raw:
            return i+1


        

from math import gcd
from collections import deque
for _ in range(int(input())):
    n = int(input())
    s = input()
    a = list(map(lambda x: int(x)-1, input().split()))

    ans = 1
    vis = [0] * n
    for i in range(n):
        if vis[i] == 0:
            cycle = deque()
            cycle.append(s[i])

            cur = i
            while a[cur] != i:
                vis[cur] = 1
                cur = a[cur]
                cycle.append(s[cur])
                
            period = find_period(cycle)
            ans = ans // gcd(ans, period) * period
    printf(ans)
        
        
