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
    s = list(input())
    m, = inp()
    qs = [input().split() for _ in range(m)]
    cur = m-1
    while cur > 0 and qs[cur][0] == '1':
        cur -= 1
    for i in range(cur):
        op, p, c = qs[i]
        if op == '1':
            s[int(p)-1] = c
        
    s = ''.join(s)
    if qs[cur][0] == '3':
        s = s.upper()
    elif qs[cur][0] == '2':
        s = s.lower()
    s = list(s)
    for i in range(cur, m):
        op, p, c = qs[i]
        if op == '1':
            s[int(p)-1] = c
    print(''.join(s))
        

cas = 1
for _ in range(cas):
    solve(_)

