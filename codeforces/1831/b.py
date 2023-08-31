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
    n, = inp()
    a = inp()
    b = inp()
    mp = make_arr(2*n+1, 2)(lambda: 0)

    cur = a[0]
    cnt = 1
    for i in range(1, n):
        if a[i] == cur:
            cnt += 1
        else:
            mp[cur][0] = max(mp[cur][0], cnt)
            cnt = 1
            cur = a[i]
    mp[cur][0] = max(mp[cur][0], cnt)
    
    cur = b[0]
    cnt = 1
    for i in range(1, n):
        if b[i] == cur:
            cnt += 1
        else:
            mp[cur][1] = max(mp[cur][1], cnt)
            cnt = 1
            cur = b[i]
    mp[cur][1] = max(mp[cur][1], cnt)

    
    ans = 0
    for i in range(1, 2*n+1):
        ans = max(ans, sum(mp[i]))

    print(ans)
            


cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

