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
    if n == 2:
        print(int(s))
        return
        
    
    def min_calc(arr):
        res = []
        for a in arr:
            if a == 0:
                return 0
            elif a != 1:
                res.append(a)

        if len(res) == 0:
            return 1
        return sum(res)

    mn = 10**9
    for i in range(n-1):
        ls = []
        for j in range(n):
            if j == i+1: continue
            if i == j:
                ls.append(int(s[i]+s[i+1]))
            else:
                ls.append(int(s[j]))
        # debug(ls)
        mn = min(mn, min_calc(ls))
    print(mn)


        
        
        

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

