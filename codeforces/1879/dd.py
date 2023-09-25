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
MOD = 998244353
def norm(v):
    v = v % MOD
    if v < 0: v += MOD
    return v

def solve(cas):
    n, = inp()
    a = inp()
    ans = 0
    for j in range(30):
        s = [0, 0]
        c = [0, 0]
        for i in range(n-1, -1, -1):
            t = a[i] >> j & 1
            if t:
                s[0], s[1] = s[1], s[0]
                c[0], c[1] = c[1], c[0]
            s[t] += i
            c[t] += 1
            ans += (s[1] - (i-1) * c[1]) * (1<<j)
            ans = norm(ans)
    print(ans)

cas = 1
for _ in range(cas):
    solve(_)

