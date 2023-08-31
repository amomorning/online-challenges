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
    a, b, c, d = inp()
    if a == 0:
        print(1)
        return

    u, v = a, a
    ans = a
    
    tmp = min(b, c)
    b -= tmp
    c -= tmp
    ans += tmp*2
    if b > 0:
        tmp = min(b, v)
        ans += tmp
        b -= tmp
        v -= tmp
        u += tmp
    elif c > 0:
        tmp = min(c, u)
        ans += tmp
        c -= tmp
        u -= tmp
        v += tmp

    tmp = min(u, v, d)
    ans += tmp
    u -= tmp
    v -= tmp
    d -= tmp

    if b+c+d > 0:
        ans += 1
    print(ans)

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
