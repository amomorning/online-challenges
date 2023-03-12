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
    p, q = 0, 0
    for i in range(n):
        s = input()
        a = m//4
        vis = [0] * m
        for j in range(m):
            if j+1 < m and vis[j:j+2] == [0, 0] and s[j:j+2] == '11' and a > 0:
                vis[j], vis[j+1] = 1, 1
                a -= 1
                p += 1
        for j in range(m):
            if j+1 < m and vis[j:j+2] == [0, 0] and a > 0:
                vis[j], vis[j+1] = 1, 1
                a -= 1
                if s[j] == '1' or s[j+1] == '1': p += 1
        
        for j in range(m):
            if vis[j] == 0 and s[j] == '1':
                p += 1

        a = m//4
        vis = [0] * m
        for j in range(m):
            if j+1 < m and vis[j:j+2] == [0, 0] and s[j:j+2] != '11' and a > 0:
                vis[j], vis[j+1] = 1, 1
                a -= 1
                if s[j] == '1' or s[j+1] == '1': q += 1

        for j in range(m):
            if j+1 < m and vis[j:j+2] == [0, 0] and a > 0:
                vis[j], vis[j+1] = 1, 1
                a -= 1
                if s[j] == '1' or s[j+1] == '1': q += 1
        for j in range(m):
            if vis[j] == 0 and s[j] == '1':
                q += 1                
    print(p, q)
    

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

