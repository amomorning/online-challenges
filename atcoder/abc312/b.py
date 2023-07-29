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
    s = [input() for _ in range(n)]

    for i in range(n-8):
        for j in range(m-8):
            flag = True
            for k in range(3):
                for l in range(3):
                    if s[i+k][j+l] != '#':
                        flag = False
                    if s[i+8-k][j+8-l] != '#':
                        flag = False
                if s[i+k][j+3] != '.':
                    flag = False
                if s[i+8-k][j+5] != '.':
                    flag = False
                if s[i+3][j+k] != '.':
                    flag = False
                if s[i+5][j+8-k] != '.':
                    flag = False
            if s[i+3][j+3] != '.':
                flag = False
            if s[i+5][j+5] != '.':
                flag = False
            if flag:
                print(i+1, j+1)



cas = 1
for _ in range(cas):
    solve(_)

