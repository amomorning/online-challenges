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
    s = [input() for _ in range(n)]
    t = [list(s[i]) for i in range(n)]
    
    # U, D
    for i in range(n):
        cnt = 0
        for j in range(m):
            if s[i][j] == 'U':
                cnt += 1
        if cnt % 2 != 0 or (cnt > 0 and i == n-1):
            print(-1)
            return
        cur = 0
        for j in range(m):
            if s[i][j] == 'U':
                if cur < cnt//2:
                    t[i][j] = 'B' 
                    t[i+1][j] = 'W'
                else:
                    t[i][j] = 'W'
                    t[i+1][j] = 'B'
                cur += 1
    # L, R
    for j in range(m):
        cnt = 0
        for i in range(n):
            if s[i][j] == 'L':
                cnt += 1
        if cnt % 2 != 0 or (cnt > 0 and j == m-1):
            print(-1)
            return
        cur = 0
        for i in range(n):
            if s[i][j] == 'L':
                if cur < cnt // 2:
                    t[i][j] = 'B'
                    t[i][j+1] = 'W'
                else:
                    t[i][j] = 'W'
                    t[i][j+1] = 'B'
                cur += 1
    for i in range(n):
        print(''.join(t[i]))
            


cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

