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
    a = inp(lambda x: int(x)-1)

    p = [None] * n
    for i in range(n):
        p[a[i]] = i

    q = collections.deque()
    if n % 2 != 0:
        q.append(p[n//2])
        u, v = p[n//2], p[n//2]
        l, r = n//2-1, n//2+1 
    else:
        l, r = n//2-1, n//2
        u, v = -1, -1

    
    cnt = 0
    while l >= 0 and r < n and p[l] < p[r] and (u == -1 or (p[l] < u and p[r] > v)):
        cnt += 1
        u, v = p[l], p[r]
        l -= 1
        r += 1

    print(n // 2 - cnt)

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
