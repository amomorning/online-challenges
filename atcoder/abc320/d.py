import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x() for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

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

# avaliable on Google, AtCoder
# sys.setrecursionlimit(10**6)
# import numpy as np
# import scipy

# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def solve(cas):
    n, m = inp()
    G = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, x, y = inp()
        G[a].append((b, x, y))
        G[b].append((a, -x, -y))
    
    pos = [None] * (n+1)
    pos[1] = (0, 0)
    def bfs():
        q = collections.deque([1])
        while q:
            u = q.popleft()
            for v, x, y in G[u]:
                if pos[v] == None:
                    pos[v] = (pos[u][0] + x, pos[u][1] + y)
                    q.append(v)
                else:
                    if pos[v] != 'undecidable':
                        if pos[v][0] != pos[u][0] + x or pos[v][1] != pos[u][1] + y:
                            pos[v] = 'undecidable'
        
            
    bfs()
    for i in range(1, n+1):
        if pos[i] is None:
            print('undecidable')
        else:
            printf(pos[i])
    

cas = 1
for _ in range(cas):
    solve(_)

