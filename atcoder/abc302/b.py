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
d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def solve(cas):
    H, W = inp()
    S = [input() for _ in range(H)]
    T = 'snuke'

    for i in range(H):
        debug(S[i])
        for j in range(W):
            for dx, dy in d8:
                flag = True
                for k in range(5):
                    if i+dx*k < 0 or i+dx*k >= H or j+dy*k < 0 \
                        or j+dy*k >= W or S[i+dx*k][j+dy*k] != T[k]:
                        flag = False
                        break
                if flag:
                    for k in range(5):
                        print(i+dx*k+1, j+dy*k+1)
                    return
                

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

