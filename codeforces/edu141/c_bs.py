import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
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
    a = inp()
    sorted_a = sorted(a)
    sum_a = list(itertools.accumulate(sorted_a))
    l, r = 0, n-1
    ans = -1
    while l <= r:
        mid = (l + r) >> 1
        if sum_a[mid] <= m:
            l = mid + 1
            ans = mid + 1 if mid+1 < n and sum_a[mid] + a[mid+1] - sorted_a[mid] <= m else mid 
        else:
            r = mid - 1
    # debug(ans)
    print(n - ans)
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
