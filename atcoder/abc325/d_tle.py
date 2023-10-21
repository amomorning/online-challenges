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
    a = [inp() for _ in range(n)]
    b = []
    for i in range(n):
        b.append((a[i][0]+a[i][1], -a[i][0]))
    b = sorted(b)
    last = {}

    vis = {}

    ans = 0
    for i in range(n):
        t = b[i][0]
        if t in last:
            tmp = last[t]
            while tmp in vis: tmp -= 1
            if tmp >= -b[i][1] and tmp > 0:
                last[t] = tmp-1
                vis[tmp] = True
                ans += 1
                # debug(tmp, b[i])
        else:
            last[t] = t-1
            vis[t] = True
            ans += 1
    print(ans)

        

cas = 1
for _ in range(cas):
    solve(_)

