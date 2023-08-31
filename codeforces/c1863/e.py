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
    n, m, k = inp()
    h = inp()
    G = [[] for _ in range(n)]
    for _ in range(m):
        u, v = inp(lambda x: int(x)-1)
        G[u].append(v)
    
    vmax = 0
    level = [0] * n
    for u in range(n):
        vmax = max(vmax, level[u] * k + h[u])
        for v in G[u]:
            level[v] = max(level[v], level[u] + int(h[v] < h[u]))

    o = list(sorted(zip(h, range(n))))
    ans = math.inf
    for _, cu in o:
        ans = min(ans, vmax - h[cu])
        q = collections.deque()
        def update(v, w):
            nonlocal vmax
            if w > level[v]:
                level[v] = w
                q.append(v)
                vmax = max(vmax, level[v] * k + h[v])
        update(cu, 1)
        while q:
            u = q.popleft()
            for v in G[u]:
                update(v, level[u] + int(h[v] < h[u]))
    print(ans)


cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

