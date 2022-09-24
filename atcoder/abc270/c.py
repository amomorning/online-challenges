import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda : list(map(int, input().split()))

def debug(*args):
    if LOCAL:
        print('\033[92m', end='')
        printf(*args)
        print('\033[0m', end='')

def printf(*args):
    if LOCAL:
        print('>>>: ', end='')
    for arg in args:
        if isinstance(arg, typing.Iterable) and \
                not isinstance(arg, str) and \
                not isinstance(arg, dict):
            print(' '.join(map(str, arg)), end=' ')
        else:
            print(arg, end=' ')
    print()


n, x, y = inp() 
x -= 1; y -= 1
G = [[] for _ in range(n) ]
for i in range(n-1):
    u, v = inp()
    u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)

q = collections.deque()
fa = [-1] * n

q.append(y)
while q:
    u = q.popleft()
    for v in G[u]:
        if fa[v] == -1:
            q.append(v)
            fa[v] = u

print(x+1, end=' ')
while fa[x] != y:
    x = fa[x]
    print(x+1, end=' ')
print(y+1)


        
    
    
