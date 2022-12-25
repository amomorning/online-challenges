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

MOD = 998244353
def norm(v):
    v = v % MOD
    if v < 0: v += MOD
    return v

def pos(c):
    return ord(c) - ord('a')

def solve(cas):
    n, = inp()
    s = input()
    F = make_arr(26, 26)(0)
    for i in range(26):
        for j in range(26):
            if i == j: F[i][j] = 0
            else: F[i][j] = 1
            if s[0] != '?':
                F[i][j] = min(F[i][j], int(j == pos(s[0])))
            if s[1] != '?':
                F[i][j] = min(F[i][j], int(i == pos(s[1])))
    
    for i in range(2, n):
        G = make_arr(26, 26)(0)
        for a in range(26):
            for b in range(26):
                if a == b: continue
                for c in range(26):
                    if c == b or c == a: continue
                    if s[i] == '?':
                        G[a][b] += F[b][c]
                    else:
                        if a == pos(s[i]):
                            G[a][b] += F[b][c]
                        else:
                            G[a][b] = 0
                G[a][b] = norm(G[a][b])
        F = G
    tot = 0
    for i in range(26):
        for j in range(26):
            tot = norm(tot + F[i][j])
    print(tot)
        
cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
