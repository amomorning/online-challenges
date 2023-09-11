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
    n, k, a, b = inp()
    coords = [inp() for _ in range(n)]
    a -= 1; b -= 1
    def distance(p, q):
        return abs(p[0]-q[0]) + abs(p[1]-q[1])
    if a < k and b < k:
        print(0)
    elif a < k:
        ans = math.inf
        for i in range(k):
            ans = min(ans, distance(coords[i], coords[b]))
        print(ans)
    elif b < k:
        ans = math.inf
        for i in range(k):
            ans = min(ans, distance(coords[i], coords[a]))
        print(ans)
    else:
        mna = math.inf
        for i in range(k):
            mna = min(mna, distance(coords[i], coords[a]))
        mnb = math.inf
        for i in range(k):
            mnb = min(mnb, distance(coords[i], coords[b]))
        print(min(mna+mnb, distance(coords[a], coords[b])))
            
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

