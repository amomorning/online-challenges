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
    N, T = inp()
    S = input()
    X = inp()
    p, q = [], []
    for i in range(N):
        if S[i] == '1':
            p.append(X[i])
        else:
            q.append(X[i])
    p.sort()
    q.sort()
    
    l, r = 0, 0
    ans = 0
    debug(p)
    debug(q)
    # print('-------')
    for x in p:
        while l < len(q) and q[l] <= x:
            l += 1
        while r < len(q) and q[r] <= x + 2*T:
            r += 1
        debug(x, l, r)
        if r > l:
            ans += r - l
    print(ans)
        

        



cas = 1
for _ in range(cas):
    solve(_)

