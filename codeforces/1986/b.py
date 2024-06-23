#!/usr/bin/env python3
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


d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def solve(cas):
    n, m = inp()
    mat = [inp() for _ in range(n)]
    for i in range(n):
        for j in range(m):
            mx = -1
            for d in d4:
                x, y = i + d[0], j + d[1]
                if 0 <= x < n and 0 <= y < m:
                    mx = max(mx, mat[x][y])
            if mx != -1 and mx < mat[i][j]:
                mat[i][j] = mx
    
    for i in range(n):
        print(' '.join(map(str, mat[i])))
                
                        

    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

