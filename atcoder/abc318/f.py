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
    x = inp()
    l = inp()

    seg = set()
    for xx in x:
        for ll in l:
            seg.add(xx-ll)
            seg.add(xx-ll+1)
            seg.add(xx-ll-1)
            seg.add(xx+ll)
            seg.add(xx+ll+1)
            seg.add(xx+ll-1)
    
    def check(k):
        L, R = 0, n-1
        if x[R] < k-l[0]: return False
        if x[L] > k+l[0]: return False
        while L < n and x[L] < k-l[0]: L += 1
        while R > 0 and x[R] > k+l[0]: R -= 1
        if R-L < 0: return False
        for i in range(1, n):
            while L > 0 and x[L-1] >= k-l[i]: L -= 1
            while R+1 < n and x[R+1] <= k+l[i]: R += 1
            if R-L < i: return False
        return True


    
    seg = list(sorted(seg))
    ans = 0
    for i in range(1, len(seg)):
        L, R = seg[i-1], seg[i]
        if check(L):
            ans += R-L
    print(ans)

cas = 1
for _ in range(cas):
    solve(_)

