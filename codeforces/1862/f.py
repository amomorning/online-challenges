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
    w, f = inp()
    if w > f: w, f = f, w
    n, = inp()
    a = inp()
    MAX = sum(a)
    dp = [math.inf] * (MAX+1)
    dp[0] = 0
    for i in range(n):
        for j in range(MAX, a[i]-1, -1):
            dp[j] = min(dp[j], dp[j-a[i]] + 1)

    all = [i for i in range(MAX+1) if dp[i] != math.inf]

    def check(k):
        for x in all:
            if x <= k*w and MAX-x <= k*f:
                return True
        return False

    l, r = math.ceil(MAX/(w+f)), math.ceil(MAX/w)
    while l <= r:
        m = (l+r)//2
        if check(m):
            ans = m
            r = m-1
        else:
            l = m+1
    # debug(all)
    print(ans)
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

