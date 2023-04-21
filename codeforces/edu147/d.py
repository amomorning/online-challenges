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
    n, k = inp()
    l = inp()
    r = inp()
    tot = sum([r[i] - l[i] + 1 for i in range(n)])
    if tot < k: 
        print(-1)
        return
    ans = math.inf
    oneseg = 0
    for i in range(n):
        curlen = r[i] - l[i] + 1
        if oneseg + curlen >= k:
            debug(oneseg, curlen, k, i)
            if curlen >= k:
                ans = min(ans, (i-oneseg)*2 + l[i] + k + 1)
            else:
                ans = min(ans, (i-oneseg)*2 + (k-curlen)*2 + r[i] + 2)
        
        if r[i] == l[i]: 
            oneseg += 1
        elif k >= curlen:
            k -= curlen
        
    print(ans)
        

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

