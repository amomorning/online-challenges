#!/usr/bin/env python3
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


# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout



def solve(cas):
    n, a, b, c = inp()
    g = [inp() for _ in range(n)]

    def dijk(s, cost):
        q = []
        d = [math.inf] * n
        d[s] = 0
        heapq.heappush(q, (d[s], s))
        while q:
            du, u = heapq.heappop(q)
            if d[u] < du: continue
            for v in range(n):
                # debug(u, v)
                if d[v] > d[u] + cost(g[u][v]):
                    d[v] = d[u] + cost(g[u][v])
                    heapq.heappush(q, (d[v], v))
        return d

    d0 = dijk(0, lambda x: a*x)
    d1 = dijk(n-1, lambda x: b*x+c)
    ans = min(d0[n-1], d1[0])
    for i in range(1, n-1):
        ans = min(ans, d0[i]+d1[i])
    print(ans)
        

cas = 1
for _ in range(cas):
    solve(_)

