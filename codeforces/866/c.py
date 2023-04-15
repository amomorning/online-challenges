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

def mex(a):
    a = list(sorted(set(a)))
    for i in range(len(a)):
        if a[i] != i: return i
    return len(a)


    
def solve(cas):
    n, = inp()
    a = inp()
    s = mex(a)
    if s == 0: 
        print("Yes")
        return

    t = s+1
    if t in a:
        mni, mxi = n, -1
        for i in range(n):
            if a[i] == t:
                mni = min(mni, i)
                mxi = max(mxi, i)
        for i in range(mni, mxi+1):
            a[i] = s
        if mex(a) == t:
            print("Yes")
        else:
            print("No")
    else:
        a = sorted(a)
        for i in range(1, n):
            if a[i] == a[i-1]:
                print("Yes")
                return
            if a[i] > s:
                print("Yes")
                return
        print("No")
        
    
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

