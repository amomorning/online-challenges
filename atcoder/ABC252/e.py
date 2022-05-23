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

from heapq import *

n, m = map(int, input().split())
G = [[] for i in range(n)]
for i in range(m):
    u, v, c = map(int, input().split())
    G[u-1].append((v-1, c, i))
    G[v-1].append((u-1, c, i))

D = [1e18] * n
D[0] = 0 
q = [(0, '', 0)]
while q:
    d, idx, u = heappop(q)
    if D[u] < d:
        continue
    
    print(idx, end=' ')

    for v, c, i in G[u]:
        if D[v] > d + c:
            D[v] = d + c
            heappush(q, (D[v], i+1, v))

