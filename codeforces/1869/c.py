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
    a = make_arr(n, m)(lambda: -1)
    if m == 1:
        print(0)
        for i in range(n):
            print(0)
        return
    if n+1 >= m:
        print(m)
        for i in range(n):
            cur = i%(m-1)
            for j in range(m):
                cur = (cur+1)%m
                a[i][j] = cur
        
    else:
        print(n+1)
        for j in range(n+1):
            for i in range(0, n-j):
                a[i][j] = i+j+1
            for i in range(n-j, n):
                a[i][j] = i+j-n
        for i in range(n):
            for j in range(n+1, m):
                a[i][j] = j

    for i in range(n):
        printf(a[i])

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

