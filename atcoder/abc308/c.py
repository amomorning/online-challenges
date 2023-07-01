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

def cmp(a, b):
    p = a[0] * b[1]
    q = a[1] * b[0]
    if p == q:
        if a[2] < b[2]:
            return -1
        elif a[2] > b[2]:
            return 1
        else:
            return 0
    elif p < q:
        return 1
    else:
        return -1
        
    

def solve(cas):
    n, = inp()
    t = []
    for i in range(n):
        a, b = inp()
        t.append((a, a+b, i))
    t = sorted(t, key = functools.cmp_to_key(cmp))
    ans = [x[2]+1 for x in t]
    printf(ans)

cas = 1
for _ in range(cas):
    solve(_)

