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
    h, w = inp()
    c = [input() for _ in range(h)]
    s = [0] * min(h, w)
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                mx = 0
                for k in range(1, min(h, w)):
                    if i+k < h and i-k >= 0 and j+k < w and j-k >= 0 and c[i+k][j+k] == '#' and c[i+k][j-k] == '#' and c[i-k][j+k] == '#' and c[i-k][j-k] == '#':
                        mx = k
                    else:
                        break
                if mx > 0:
                    s[mx-1]+=1
    printf(s)

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

