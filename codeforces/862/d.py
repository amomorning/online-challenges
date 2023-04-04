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
    n, = inp()
    G = [[] for _ in range(n)]
    for i in range(n-1):
        u, v = inp(lambda x: int(x)-1)
        G[u].append(v)
        G[v].append(u)
    
    def bfs(s, d):
        q = collections.deque([s])
        vis = [0]*n
        d[s] = 0
        while q:
            u = q.popleft()
            vis[u] = 1
            for v in G[u]:
                if not vis[v]:
                    d[v] = d[u] + 1
                    q.append(v)
            if len(q) == 0:
                return u
    du, dv = [-1]*n, [-1]*n
    u = bfs(0, [-1]*n)
    v = bfs(u, du)
    _ = bfs(v, dv)
    
    ans = [1]*n
    d = sorted([max(du[i], dv[i]) for i in range(n)])
    for i in range(n):
        p = bisect.bisect_left(d, i+1)
        ans[i] += p
        if ans[i] > n: ans[i] = n
    printf(ans)
    

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

