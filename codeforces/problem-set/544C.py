import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

def make_arr(*args):
    """ Usage:

        ```
        dp = make_arr(2, 3)(lambda:0)
        dp = make_arr(3, 4)(list)
        ```
    """
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

MOD = 998244353
def norm(v):
    v = v % MOD
    if v < 0: v += MOD
    return v

def solve(cas):
    global MOD
    n, m, b, MOD = inp()
    a = inp()

    dp = make_arr(m+1, b+1)(lambda:0)
    dp[0][0] = 1

    for k in range(n):
        for i in range(m):
            for j in range(b-a[k]+1):
                dp[i+1][j+a[k]] = norm(dp[i+1][j+a[k]] + dp[i][j])

    
    ans = 0
    for i in range(b+1):
        ans = norm(ans + dp[m][i])
    print(ans)



cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

