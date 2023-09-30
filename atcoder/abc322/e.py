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

def to_arr(num, k, base=6):
    arr = []
    for i in range(k):
        arr.append(num%base)
        num //=base
    return arr

def to_num(arr, base=6):
    cur = 1
    ret = 0
    for c in arr:
        ret += c * cur
        cur *= base
    return ret

def sub(a, b):
    ret = []
    for x, y in zip(a, b):
        ret.append(max(0, x-y))
    return ret

def solve(cas):
    n, k, p = inp()
    a = [inp() for _ in range(n)]

    MX = to_num([p]*k)
    dp = make_arr(MX+1)(lambda: math.inf)
    dp[MX] = 0
    for i in range(n):
        for j in range(MX+1):
            if dp[j] == math.inf: continue
            # debug(to_arr(j, k))
            p = sub(to_arr(j, k), a[i][1:])
            np = to_num(p)
            dp[np] = min(dp[np], dp[j]+a[i][0])
        # debug('--------------')
    print(dp[0]) if dp[0] != math.inf else print(-1)
        

cas = 1
for _ in range(cas):
    solve(_)

