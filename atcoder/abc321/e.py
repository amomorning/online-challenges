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
    N, X, K = inp()
    D = N.bit_length()-1
    C = X.bit_length()-1
    if K > C+D: 
        print(0)
        return
    ans = 0

    def down(cur, cd, depth):
        if depth < 0: return 0
        l, r = cur, cur
        for i in range(cd, cd+depth):
            if i > D: return 0
            l = l * 2
            r = r * 2 + 1
        if l > N: return 0
        return min(r, N) - l + 1
            
    # down
    ans += down(X, C, K)
    # debug(ans)
    while C:
        p = down(X//2, C-1, K-1)
        q = down(X, C, K-2)
        # debug(p, q)
        ans += p - q
        X //= 2
        K -= 1
        C -= 1
    print(ans)
    





cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)


