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

MOD = 998244353
def norm(v):
    v = v % MOD
    if v < 0: v += MOD
    return v

def solve(cas):
    n, = inp()
    a = [inp() for _ in range(n)]
    dp = make_arr(n, n)(0)
    dp[0][0] = 2

    for i in range(n):
        if a[i][0] == 2:
            print(0)
            return
    
    
    for i in range(1, n):
        for j in range(i):
            if dp[i-1][j] == 0: continue 
            if j == i-1:
                dp[i][j] += dp[i-1][j]
                dp[i][j+1] += dp[i-1][j]
            else:
                dp[i][j] += dp[i-1][j]
                dp[i][i-1] += dp[i-1][j]
            
        for j in range(i+1):
            for k in range(0, i+1):
                if a[k][i-k] == 1:
                    if j >= k and j != i:
                        dp[i][j] = 0
                if a[k][i-k] == 2:
                    if j < k or j >= i:
                        dp[i][j] = 0
            dp[i][j] = norm(dp[i][j])
    print(norm(sum(dp[n-1])))
    

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
