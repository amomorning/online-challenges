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
    N, M = inp()
    G = make_arr(N+M)(list)
    for i in range(N):
        a, = inp()
        S = inp(lambda x: int(x)-1)
        for j in range(a):
            G[S[j]].append(i+M)
            G[i+M].append(S[j])
    
    def bfs(s, t):
        d = [math.inf] * (N+M)
        d[s] = 0
        q = []
        heapq.heappush(q, (d[s], s))
        while q:
            du, u = heapq.heappop(q)
            for v in G[u]:
                if d[v] > du + 1:
                    d[v] = du+1
                    heapq.heappush(q, (d[v], v))
            
        debug(d)
        return d[t]

    ans = bfs(0, M-1)
    if ans == math.inf:
        print(-1)
    else:
        print(ans//2-1)

cas = 1
for _ in range(cas):
    solve(_)

