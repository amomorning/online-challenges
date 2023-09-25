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
    n, = inp()
    a = inp()
    G = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = inp(lambda x: int(x)-1)
        G[u].append(v)
        G[v].append(u)

    sz = [0] * n
    topo = []
    p = [-1] * n
    def count():
        q = collections.deque([0])
        vis = [0] * n
        while q:
            u = q.popleft()
            vis[u] = 1
            topo.append(u)
            for v in G[u]:
                if not vis[v]:
                    q.append(v)
                    p[v] = u
        
        for u in reversed(topo):
            sz[u] = 1
            for v in G[u]:
                if v != p[u]:
                    sz[u] += sz[v]
        
    count()

    result = [0] * n
    for bit in range(20):
        dp = make_arr(n, 2)(lambda:0)
        for u in reversed(topo):
            for v in G[u]:
                if v != p[u]:
                    for i in range(2):
                        dp[u][i] += dp[v][i]
            c = a[u] >> bit & 1
            dp[u][c^1] = dp[u][c] + sz[u]
        
        # debug(dp)
        sum = make_arr(n, 2)(lambda:0)

        for u in topo:
            for v in G[u]:
                if v != p[u]:
                    sum[u][0] += dp[v][0]
                    sum[u][1] += dp[v][1]
            c = a[u] >> bit & 1
            result[u] += (1<<bit) * sum[u][c]
            for v in G[u]:
                if v != p[u]:
                    tmp = [sum[u][0], sum[u][1]]
                    tmp[0] -= dp[v][0]
                    tmp[1] -= dp[v][1]
                    tmp[c^1] = tmp[c] + n - sz[v]
                    sum[v] = tmp
    printf(result)
            





cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

