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

d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def solve(cas):
    n, m = inp()
    s = [input() for _ in range(n)]
    q = collections.deque([(1, 1)])
    vis = make_arr(n, m)(lambda: 0)
    vis[1][1] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d4:
            xx, yy = x+dx, y+dy
            if s[xx][yy] == '#': continue
            flag = False
            while s[xx][yy] == '.':
                if vis[xx][yy] == 0: flag = True
                xx += dx
                yy += dy
            xx -= dx
            yy -= dy
            if not vis[xx][yy]: q.append((xx, yy))
            if flag:
                vis[xx][yy] = 1
                while xx != x or yy != y:
                    vis[xx][yy] = 1
                    xx -= dx
                    yy -= dy
    for i in range(n):
        debug(vis[i])
    print(sum([sum(vis[i]) for i in range(n)]))

cas = 1
for _ in range(cas):
    solve(_)

