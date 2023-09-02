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
    n, = inp()
    d = make_arr(n, n)(lambda:math.inf)
    for i in range(n):
        for j, w in enumerate(inp()):
            d[i][j+i+1] = w
            d[j+i+1][i] = w
    
    MAX = 2**(n+1) 
    dp = [0] * MAX
    for b in range(1, MAX-1):
        for i in range(n):
            if b >> i & 1: continue
            for j in range(n):
                if j == i: continue
                if b >> j & 1: continue
                a = b+(1<<i)+(1<<j)
                if a > MAX: continue
                dp[a] = max(dp[a], dp[b] + d[i][j])
    print(dp[MAX-1])
            


cas = 1
for _ in range(cas):
    solve(_)

