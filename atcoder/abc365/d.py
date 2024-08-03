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
    n, = inp()
    s = input()
    won = {'P': 'S', 'S': 'R', 'R': 'P'}
    idx = {'P': 0, 'S': 1, 'R': 2}
    dp = make_arr(n+1, 3)(lambda:0)

    for i in range(n):
        cur = won[s[i]]
        j = idx[cur]
        k = idx[s[i]]
        dp[i+1][j] = max(dp[i][(j+1)%3], dp[i][(j+2)%3]) + 1
        dp[i+1][k] = max(dp[i][(k+1)%3], dp[i][(k+2)%3])
    print(max(dp[n]))
            


        
        
        
        

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

