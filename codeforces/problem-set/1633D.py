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
M = int(1e3)
q = collections.deque()
q.append(1)
d = [math.inf] * (M+1)
d[1] = 0
while q:
    u = q.popleft()
    for x in range(1, u+1):
        v = u + u//x
        if v <= 1000 and d[v] > d[u] + 1:
            d[v] = d[u] + 1
            q.append(v)

def solve(cas):
    n, k = inp()
    b = inp()
    c = inp()
    
    k = min(k, 12*n)
    F = [0] * (k+1)
    for i in range(n):
        for v in range(k, d[b[i]]-1, -1):
            F[v] = max(F[v], F[v - d[b[i]]] + c[i])
    
    print(F[k])
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

