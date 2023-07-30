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
    N, = inp()
    M = 101
    cube = make_arr(M, M, M)(lambda:-1)
    for i in range(N):
        x0, y0, z0, x1, y1, z1 = inp()
        for x in range(x0, x1):
            for y in range(y0, y1):
                for z in range(z0, z1):
                    cube[x][y][z] = i
    ans = make_arr(N)(set)
    for i in range(M-1):
        for j in range(M-1):
            for k in range(M-1):
                p = cube[i][j][k]
                for q in [cube[i+1][j][k], cube[i][j+1][k], cube[i][j][k+1]]:
                    if p!=-1 and q!=-1 and p!=q:
                        ans[p].add(q)
                        ans[q].add(p)
    for i in range(N):
        print(len(ans[i]))


cas = 1
for _ in range(cas):
    solve(_)

