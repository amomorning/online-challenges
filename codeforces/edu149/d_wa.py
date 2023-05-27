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

def find_seg(lasti, s):
    cur = 1
    for i in range(lasti+1, len(s)):
        if s[i] == s[lasti]:
            cur += 1
        else:
            cur -= 1
        if cur < 0:
            return i
    return len(s)

def solve(cas):
    n, = inp()
    s = input()
    if n % 2 == 1:
        print(-1)
        return
    
    ans = []
    lasti = 0
    while True:
        curi = find_seg(lasti, s)
        ans.append((lasti, curi))
        lasti = curi
        if lasti == n: break

    if len(ans) > 1: print(2)            
    else: print(1)

    cur = 0
    res = [-1] * n
    for l, r in ans:
        for i in range(l, r):
            res[i] = cur+1
        cur ^= 1
    printf(res)
            


cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

