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
    n, = inp()
    s = [input() for _ in range(2)]
    t = [[], []]
    i = 0
    while i < n:
        if i < n-1 and s[1][i] == 'B' and s[0][i] == 'B' and s[1][i+1] == 'B' and s[0][i+1] == 'B':
            i += 2
            continue
        t[0].append(s[0][i])
        t[1].append(s[1][i])
        i += 1
    m = len(t[0])
    if m < 2:
        print("YES")
        return
    i = 1 if t[0][0] == 'B' and t[1][0] == 'B' else 0
    now = -1
    if t[0][i] == 'B':
        now = 0
    if t[1][i] == 'B':
        now = 1
    if now == -1:
        print("NO")
        return

    while i < m:
        if t[0][i] == 'B' and t[1][i] == 'B':
            now = 1 - now
        elif t[now][i] == 'B':
            pass
        else:
            print("NO")
            return
        i += 1
    print("YES")
    return
    
    

        

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
