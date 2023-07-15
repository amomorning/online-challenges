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
    a = []
    for i in range(n):
        p, _, *b = inp()
        a.append((p, b))
    for i in range(n):
        for j in range(n):
            if a[i][0] >= a[j][0]:
                vis = [0] * m
                flag = True
                for k in a[j][1]:
                    vis[k-1] = 1
                for k in a[i][1]:
                    if vis[k-1] == 0:
                        flag = False
                    vis[k-1] += 1
                if not 1 in vis and a[i][0] == a[j][0]:
                    flag = False
                if flag:
                    print("Yes")
                    return 
    print("No")
                
        

cas = 1
for _ in range(cas):
    solve(_)

