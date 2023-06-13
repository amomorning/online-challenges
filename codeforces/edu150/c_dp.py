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

MX = 5

def solve(cas):
    s = list(map(lambda c: ord(c) - ord('A'), list(input())))
    n = len(s)
    F = make_arr(MX, 2)(lambda:-math.inf) # 0 - non 1 - modify
    F[0][0] = 0
    for i in range(n-1, -1, -1):
        G = make_arr(MX, 2)(lambda:-math.inf)
        for j in range(MX):
            G[max(j, s[i])][1] = max(G[max(j, s[i])][1], F[j][1] + (-1)**(s[i]<j) * 10**s[i])
            for k in range(MX):
                G[max(j, k)][k!=s[i]] = max(G[max(j, k)][k!=s[i]], F[j][0] + (-1)**(k<j) * 10**k)

        F = G
    
    print(max(map(max, F)))
                        
                

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

