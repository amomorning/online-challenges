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
    n, m = inp()
    MAXB = (10**9).bit_length()+1
    a = inp()
    b = inp()
    def calc(arr):
        cur = 0
        for c in arr:
            cur ^= c
        return cur
    mn, mx = calc(a), calc(a)

    for j in range(m):
        cur = []
        for c in a:
            cur.append(c)
        for i in range(n):
            cur[i] = cur[i] | b[j]
        mn = min(mn, calc(cur))
        mx = max(mx, calc(cur))
    print(mn, mx)
    

            



cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

