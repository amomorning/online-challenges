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

def fun(Q):
    debug(Q)
    k = len(Q)
    sum = 0
    tot = 0
    for i in range(k):
        tmp = (0.9)**(k-i-1)
        debug(tmp)
        tot += tmp
        sum += tmp * Q[i]
    return sum/tot - 1200/math.sqrt(k)

def solve(cas):
    n, = inp()
    P = inp()
    F = [-math.inf] * (n+1)
    F[0] = 0
    cur = 1
    tmp = [1]
    for i in range(n):
        tmp.append(cur)
        cur = cur*0.9 + 1

    for i in range(n):
        G = [-math.inf] * (n+1)
        for j in range(n): 
            if F[j] == -math.inf: continue
            G[j] = max(G[j], F[j])
            if j == 0:
                G[j+1] = max(G[j+1], ((F[j] * 0.9)*tmp[j] + P[i])/tmp[j+1] - 1200/math.sqrt(j+1))
            else:
                G[j+1] = max(G[j+1], ((F[j] + 1200/math.sqrt(j))*tmp[j]*0.9 + P[i])/tmp[j+1] - 1200/math.sqrt(j+1))
        F = G
    print(max(F[1:]))

cas = 1
for _ in range(cas):
    solve(_)

