import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
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
    n, s = inp()
    a = inp()
    l = [math.inf] * n
    r = [math.inf] * n
    l[0] = 0; r[0] = 0
    l[n-1] = a[n-1]; r[n-1] = a[n-1]
    for i in range(1, n-1):
        if a[i] > 2*s:
            l[i] = s
            r[i] = a[i] - s
        else:
            l[i] = max(0, a[i] - s)
            r[i] = min(a[i], s)
    
    debug(l)
    debug(r)
    
    F = [a[0] * l[1], a[0] * r[1]]
    for i in range(1, n-1):
        G = [None, None]
        G[0] = min(F[0] + r[i] * l[i+1], F[1] + l[i] * l[i+1])
        G[1] = min(F[0] + r[i] * r[i+1], F[1] + l[i] * r[i+1])
        F = G
    print(min(F[0], F[1]))

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
