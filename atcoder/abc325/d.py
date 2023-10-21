#!/usr/bin/env python3
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


# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def solve(cas):
    n, = inp()
    a = sorted([inp() for _ in range(n)], key=lambda x: x[0])
    # debug(a)
    cur = 1
    i = 0
    q = []
    ans = 0
    while i < n or q:
        if i < n and a[i][0] <= cur:
            heapq.heappush(q, a[i][0] + a[i][1])
            i += 1
            continue
        while q and q[0] < cur:
            heapq.heappop(q)
        if len(q) == 0 and i < n:
            cur = a[i][0]
        if q and cur <= q[0]:
            ans += 1
            cur += 1
            heapq.heappop(q)
    
    # debug(check)
    print(ans)
            
cas = 1
for _ in range(cas):
    solve(_)

