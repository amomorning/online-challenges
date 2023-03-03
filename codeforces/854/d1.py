#!/usr/bin/env python3
import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')

# LOCAL = False

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
def crange(start, end, step=1):
    dir = 1 if start < end else -1
    if start > end and step > 0: step = -step
    return range(start, end + dir, step)

def solve(cas):
    n, k = inp()
    a = inp()
    cold = [0] + inp()
    hot = [0] + inp()

    F = [(math.inf, 0)] * (k+1)
    F[0] = (0, 0)
    for x in a:
        G = [(math.inf, 0)] * (k+1)
        for i in crange(0, k):
            if F[i][1] == x:
                G[i] = min(G[i], (F[i][0] + hot[x], F[i][0]))
            elif F[i] + cold[x] < G[i]:
                G[i] = F[i] + cold[x]

        debug(x, ":", G)
        for i in crange(0, k):
            tmp = hot[x] if i == x else cold[x]
            if F[i] + tmp < G[x]:
                G[x] = F[i] + tmp

        debug(x, ":", G)
        debug(nlast)
        last = nlast
        F = G
    print(min(F[1:]))
    



cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

