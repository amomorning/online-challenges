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
    n, m = inp()
    ans = 0
    mn = 0
    for i in range(n):
        s = input()
        vis = [0] * m
        cnt2 = 0
        for j in range(m):
            if s[j] == '0' and vis[j] == 0:
                if j and vis[j-1] == 0 and s[j-1] == '1' and cnt2 < m//4:
                    ans += 1
                    cnt2 += 1
                    vis[j] = 2
                    vis[j-1] = 2
                    continue
                if j+1 < m and vis[j+1] == 0 and s[j+1] == '1' and cnt2 < m//4:
                    ans += 1
                    cnt2 += 1
                    vis[j] = 2
                    vis[j+1] = 2
                    continue
        cnt = 0
        for j in range(m):
            if j and j < m-1 and vis[j-1] == 1 and vis[j+1] == 1 and vis[j] == 0:
                cnt += 1
                vis[j] = 1
        for j in range(m):
            if s[j] == '1' and vis[j] == 0 and cnt < m//2:
                vis[j] = 1
                cnt += 1
                ans += 1
        for j in range(m):
            if j+1 < m and vis[j] == 0 and s[j] == '1' and vis[j+1] == 0 and cnt2 < m//4:
                cnt2 += 1
                ans += 1
                vis[j] = 2
                vis[j+1] = 2

        vis = [0] * m
        cnt = 0
        for j in range(m):
            if s[j] == '1' and vis[j] == 0:
                if j+1 < m and vis[j+1] == 0 and s[j+1] == '1' and cnt < m//4:
                    cnt += 1
                    vis[j] = 2
                    vis[j+1] = 2
                    # debug(j, j+1)
                    continue
        # debug(cnt)
        mn += cnt
        cnt = 0
        for j in range(m):
            if s[j] == '1' and vis[j] == 0 and cnt < m//2:
                cnt += 1
                vis[j] = 1
        mn += cnt
        # debug(cnt)
    print(mn, ans)
                


        
                

                

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

