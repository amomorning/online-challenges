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
    H, W = inp()
    s = [input() for _ in range(H)]
    Q, = inp()
    x, y, d = 0, 0, 1
    for _ in range(Q):
        a, b = inp(lambda x: int(x)-1)
        x = (x + a*d + H) % H
        y = (y + b*d + W) % W
        d = -d
    
    t = make_arr(H, W)('#')
    for i in range(H):
        for j in range(W):
            ni, nj = (x + i*d + H) % H, (y + j*d + W) % W
            t[i][j] = s[ni][nj]
    
    for i in range(H):
        print(''.join(t[i]))


cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
