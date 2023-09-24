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


# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MOD = 998244353
def norm(v):
    v = v % MOD
    if v < 0: v += MOD
    return v

def solve(cas):
    q, k = inp()
    bag = [0] * (k+1)
    bag[0] = 1
    for i in range(q):
        op, x = input().split()
        x = int(x)
        if op == '+':
            for j in range(k-x, -1, -1):
                bag[j+x] += bag[j]
                bag[j+x] = norm(bag[j+x])
        elif op == '-':
            for j in range(x, k+1):
                bag[j] -= bag[j-x]
                bag[j] = norm(bag[j])
        print(norm(bag[k]))



cas = 1
for _ in range(cas):
    solve(_)

