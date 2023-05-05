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
    b = inp()
    mx = max(b)
    idx = [i for i in range(n) if b[i] == mx]
    if len(idx) >= 3:
        ruler = idx[-1] - idx[0]
        for i in range(len(idx)-2):
            if idx[i+2] - idx[i] < ruler:
                ruler = idx[i+2] - idx[i]
        ans = mx*3 - ruler
    else:
        bb = sorted(list(zip(b, range(n))), reverse=True)
        l, m, r = bb[:3]
        for i in range(l[1]+1, m[1]):
            if b[i]+i > l[0]+l[1]:
                l = (b[i], i)
        for i in range(r[1]-1, m[1], -1):
            if b[i]-i > r[0]-r[1]:
                r = (b[i], i)

        ans = l[0]+m[0]+r[0]-r[1]+l[1]
    print(ans)
            
        

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

