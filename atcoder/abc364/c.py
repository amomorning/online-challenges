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
    N, X, Y = inp()
    A = inp()
    B = inp()

    C = sorted([(a, b) for a, b in zip(A, B)], key=lambda x: x[0], reverse=True)
    tot = 0
    cntX = 0
    for i in range(N):
        tot += C[i][0]
        cntX += 1
        if tot > X:
            break
    C = sorted([(a, b) for a, b in zip(A, B)], key=lambda x: x[1], reverse=True)
    cntY = 0
    tot = 0
    for i in range(N):
        tot += C[i][1]
        cntY += 1
        if tot > Y:
            break
    # debug(cntX, cntY)
    print(min(cntX, cntY))
    

cas = 1
for _ in range(cas):
    solve(_)

