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
    n, = inp()
    a = inp()
    b = inp()
    mp = dict()
    ans = dict()
    for i in range(n):
        if (a[i], b[i]) in mp:
            mp[a[i], b[i]] += 1
        else:
            mp[a[i], b[i]] = 1
            ans[a[i], b[i]] = -1
    
    tot = 0
    for i in range(n):
        if ans[a[i], b[i]] != -1: 
            tot += ans[a[i], b[i]]
            continue
        ans[a[i], b[i]] = 0
        aa = (b[i] + a[i] - 1) // a[i]
        # debug('[', a[i], b[i], ']')
        bb = min((n+b[i])//a[i], a[i])
        for p in range(aa, n+1): 
            q = p * a[i] - b[i]
            if q > n: break
            if p == a[i] and q == b[i]: 
                tot += mp[p, q] - 1
                ans[a[i], b[i]] += mp[p, q] - 1
                continue
            if (p, q) in mp:
                tot += mp[p, q]
                # debug(p, q)
                ans[a[i], b[i]] += mp[p, q]
        # debug('--------')
    print(tot//2)
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

