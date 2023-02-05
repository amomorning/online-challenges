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
    n, = inp()
    a, b = [0, 0], [0, 0]
    f = 1
    tot = 0 
    for i in range(1, n+10):
        cur = i
        if tot + i >= n:
            cur = n - tot
        if f:
            if cur % 2 == 0:
                a[0] += cur // 2
                a[1] += cur // 2
            elif tot % 2 == 0:
                a[0] += cur // 2 + 1
                a[1] += cur // 2
            else:
                a[0] += cur // 2
                a[1] += cur // 2 + 1
        else:
            if cur % 2 == 0:
                b[0] += cur // 2
                b[1] += cur // 2
            elif tot % 2 == 0:
                b[0] += cur // 2 + 1
                b[1] += cur // 2
            else:
                b[0] += cur // 2
                b[1] += cur // 2 + 1
        if i % 2:
            f = 1-f

        tot += cur
        if tot == n:
            break
    printf(a, b)

        


cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
