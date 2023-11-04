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

def solve(cas):
    a = [inp() for _ in range(9)]
    sig = 0
    for i in range(1, 10):
        sig ^= i
    for i in range(9):
        h, v = sig, sig
        for j in range(9):
            h ^= a[i][j]
            v ^= a[j][i]
        if v != 0 or h != 0: return False
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            t = sig
            for i in range(3):
                for j in range(3):
                    t ^= a[x+i][y+j]
            if t != 0: return False

    return True

cas = 1
for _ in range(cas):
    print('Yes') if solve(_) else print('No')

