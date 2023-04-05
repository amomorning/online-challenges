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



def check(t, k, x, y):
    fy = sorted([-100*yy[0] + t * (yy[0]+yy[1]) for yy in y])
    tot = 0
    for xx in x:
        tmp = 100*xx[0] - t * (xx[0]+xx[1])
        tot += bisect.bisect_right(fy, tmp)

    return tot >= k 
        
def solve(cas):
    n, m, k = inp()
    x = list(sorted([tuple(inp()) for _ in range(n)]))
    y = list(sorted([tuple(inp()) for _ in range(m)]))

    l, r = 0, 100
    for _ in range(100):
        m = (l+r)/2
        if check(m, k, x, y): # tot <= K
            l = m
            ans = m
        else:
            r = m
    print(ans)
            

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

