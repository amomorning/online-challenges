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
    s = [0]
    for i in range(1, n):
        if i % 2 == 0:
            s.append(s[-1]+(a[i] - a[i-1]))
        else:
            s.append(s[-1])
    
    
    for _ in range(int(input())):
        l, r = inp()
        p = bisect.bisect_left(a, l)
        q = bisect.bisect_left(a, r)
        sl, sr = 0, 0
        if (p-1)%2 == 1:
            sl = a[p] - l
        if (q-1)%2 == 1:
            sr = r - a[q-1]
        print(s[q-1] - s[p] + sl + sr)
            

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

