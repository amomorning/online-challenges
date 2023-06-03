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
    w, h = inp()
    n, = inp()
    x = [inp() for _ in range(n)]
    a, = inp()
    a = [0] + inp()
    b, = inp()
    b = [0] + inp()
    cnt = dict()
    for i in range(n):
        p = bisect.bisect_left(a, x[i][0])-1
        q = bisect.bisect_left(b, x[i][1])-1
        cnt[a[p], b[q]] = cnt.get((a[p], b[q]), 0) + 1
    mn, mx = min(cnt.values()), max(cnt.values())
    
    if len(cnt) < len(a) * len(b):
        mn = 0
    
    print(mn, mx)
        


cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

