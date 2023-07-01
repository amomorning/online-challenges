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

def cmp(a, b):
    if a[0] < b[0]:
        return -1
    if a[0] > b[0]:
        return 1
    if a[1] < b[1]:
        return 1
    if a[1] > b[1]:
        return -1
    return 0

def solve(cas):
    n, m = inp()
    p = sorted(inp())
    v = zip(inp(), inp())
    v = sorted(v, key=functools.cmp_to_key(cmp))

    i, j = 0, 0
    cur, tot = [], 0
    while i < n:
        while i < n and p[i] < v[0][0]: 
            tot += p[i]
            i += 1
        while j < m and v[j][0] <= p[i]:
            heapq.heappush(cur, -v[j][1])
            j += 1

        u = heapq.heappop(cur) if cur else 0
        tot += p[i] + u
        i += 1
        
    print(tot)
    




cas = 1
for _ in range(cas):
    solve(_)

