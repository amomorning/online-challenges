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
    s = [list(map(int, list(input()))) for _ in range(n)]
    t = make_arr(n, n)(lambda: 0)
    cnt = 0
    for j in range(n):
        t[0][j] = s[0][j]
        cnt += t[0][j]

    for i in range(1, n):
        for j in range(n):
            tmp = 0
            if j > 0:
                tmp ^= t[i-1][j-1]
            if j < n-1:
                tmp ^= t[i-1][j+1]
            if 0 < j < n-1 and i > 1:
                tmp ^= t[i-2][j]
            tmp ^= t[i-1][j]
            tmp ^= s[i][j]
            if tmp == 1:
                # debug(i, j)
                cnt += 1
            t[i][j] ^= tmp
            if j > 0:
                t[i][j] ^= t[i-1][j-1]
            if j < n-1:
                t[i][j] ^= t[i-1][j+1]
            if 0 < j < n-1 and i > 1:
                t[i][j] ^= t[i-2][j]
        # for j in range(i+1):
        #     debug(''.join(map(str, t[j])))

    print(cnt)
            


cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

