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
    n, m = inp()
    a = inp()
    b = list(sorted(zip(a, range(n))))

    cur, rk = 0, 0
    vis = [0] * n
    for i in range(n):
        cur += b[i][0]
        vis[b[i][1]] = 1

        if cur <= m:
            if i == n-1:
                rk = n
                break
            if vis[i+1]:
                rk = max(rk, i+2)
            else:
                rk = max(rk, i+1)
                if cur - b[i][0] + a[i+1] <= m:
                    rk = max(rk, i+2)
    print(n+1-rk)



    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
