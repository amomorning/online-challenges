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
    n, m = inp()
    c, p, s, t = [], [], [], []
    for i in range(n):
        cc, pp, *ss = inp()
        c.append(cc)
        p.append(pp)
        s.append(ss)
        t.append(1-(ss.count(0))/pp)

    dp = make_arr(m)(lambda: 0)
    for i in range(m-1, -1, -1):
        res = []
        for j in range(n):
            tot = 0
            for k in range(p[j]):
                if i + s[j][k] >= m:
                    tot += 0
                else:
                    tot += dp[i+s[j][k]]
            res.append((c[j]+tot/p[j])/t[j])
        dp[i] = min(res)
    print(dp[0])



cas = 1
for _ in range(cas):
    solve(_)

