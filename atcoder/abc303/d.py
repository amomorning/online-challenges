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
    X, Y, Z = inp()
    S = input()
    F = [0, math.inf] # 0 - off, 1 - on
    for c in S:
        G = [math.inf, math.inf]
        if c == 'A':
            G[0] = min(G[0], F[0]+Y, F[0]+Z+X+Z, F[1]+X+Z, F[1]+Z+Y)
            G[1] = min(G[1], F[0]+Y+Z, F[0]+Z+X, F[1]+X, F[1]+Z+Y+Z)
        else:
            G[0] = min(G[0], F[0]+X, F[0]+Z+Y+Z, F[1]+Z+X, F[1]+Y+Z)
            G[1] = min(G[1], F[0]+Y+Z, F[0]+Z+X, F[1]+Y, F[1]+Z+X+Z)
        F = G
    print(min(F[0], F[1]))

cas = 1
for _ in range(cas):
    solve(_)

