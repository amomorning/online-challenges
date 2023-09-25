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
    a = inp()
    debug(map(bin, a))
    ans = 0
    for j in range(32):
        l, r = -1, -1
        for i in range(n):
            if a[i] & (1 << j): 
                r = i+1
                if l == -1: l = i
                if r == n:
                    m = (r-l)
                    p = (m+2)*(m+1)//2*m
                    q = (m+1)*m*(2*m+1)//6 + m*(m+1)//2
                    debug(j, p-q, l, r)
                    ans += (1<<j) * (p-q)
            else:
                if r != -1:
                    m = (r-l)
                    p = (m+2)*(m+1)//2*m
                    q = (m+1)*m*(2*m+1)//6 + m*(m+1)//2
                    debug(j, p-q, l, r)
                    ans += (1<<j) * (p-q)
                l = i+1
                r = -1


    print(ans)


cas = 1
for _ in range(cas):
    solve(_)

