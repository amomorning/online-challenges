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

def solve(cas):
    m, = inp()
    cnt = inp()
    
    N, LCM = 8, 840
    dp = [-1] * (N * LCM + 1)
    dp[0] = 0

    for i in range(1, N+1):
        for j in range(min(N*LCM, m), -1, -1):
            d = -1
            for k in range(min(LCM//i, cnt[i-1]+1)):
                if j-i*k >= 0 and dp[j-i*k] != -1:
                    d = max(d, dp[j - i*k] + (cnt[i-1]-k) * i // LCM)
            dp[j] = d
    
    ans = 0
    for j in range(min(N*LCM + 1, m+1)):
        if dp[j] != -1:
            ans = max(ans, j + min(dp[j], (m-j)//LCM) * LCM)
    print(ans)
            


cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

