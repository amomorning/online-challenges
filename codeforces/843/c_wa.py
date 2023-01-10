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

def calc(arr):
    ans = 0
    for i, a in enumerate(arr):
        if a == 1:
            ans += 1 << i
    return ans

def solve(cas):
    n, x = inp()
    if x > n:
        print(-1)
        return
    if x == n:
        print(x)
        return

    s = bin(n)[2:][::-1]
    t = bin(x)[2:][::-1]

    zeros = set()
    ones = []

    ans = [-1] * (len(s)+1)
    for i in range(0, min(len(s), len(t))):
        if s[i] == t[i]: 
            if s[i] == '1':
                ones.append(i)
                ans[i] = 1
            continue
        if s[i] == '0':
            print(-1)
            return
        if s[i] == '1':
            ans[i] = 0
            zeros.add(i)
    for i in range(len(t), len(s)):
        if s[i] == '1':
            zeros.add(i)
            ans[i] = 0
    
    res = math.inf

    last = len(s)
    debug(ans)
    debug(s)
    debug(ones)
    for i in range(len(s)-1, -1, -1):
        if ans[i] == -1 and s[i] == '0':
            last = i
        if ans[i] == -1 and s[i] == '1':
            debug(i)
            ans[last] = 1
            res = min(res, calc(ans))
            ans[i] = 1
            ans[last] = -1
        if ans[i] == 0 and s[i] == '1':
            ans[last] = 1
            res = min(res, calc(ans))
            
    if res == math.inf:
        print(-1)
    else: print(res)
           
cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)

