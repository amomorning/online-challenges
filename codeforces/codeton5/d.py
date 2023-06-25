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
    edges = [[] for _ in range(n)]
    for i in range(m):
        u, v, w = inp()
        u -= 1; v -= 1
        edges[u].append((v, w))
        edges[v].append((u, w))
    
    F = [1] * n
    F[n-1] = 0
    games = []
    timer = make_arr(n, n)(lambda: 0)
    while True:
        G = [F[i] for i in range(n)]
        mn = math.inf
        for i in range(n):
            if F[i] == 0:
                for v, w in edges[i]:
                    if F[v] == 1:
                        mn = min(mn, w - timer[v][i])
        if mn != math.inf:
            for i in range(n):
                if F[i] == 0:
                    for v, w in edges[i]:
                        if F[v] == 1:
                            timer[v][i] += mn
                            if timer[v][i] == w:
                                G[v] = 0
            games.append((''.join(map(str, F)), mn))
        else:
            print('inf')
            return
        F = G
        if F[0] == 0:
            break
    print(sum([x[1] for x in games]), len(games))
    for i in range(len(games)):
        print(*games[i])
    

        


cas = 1
for _ in range(cas):
    solve(_)

