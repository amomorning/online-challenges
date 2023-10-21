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
    n, m = inp()
    s = [input() for _ in range(n)]
    vis = make_arr(n, m)(lambda: False)
    def bfs(x, y):
        q = collections.deque([(x, y)])
        vis[x][y] = True
        while q:
            ux, uy = q.popleft()

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == j and i == 0: continue
                    vx = ux+i
                    vy = uy+j
                    if vx < 0 or vx >= n or vy < 0 or vy >= m: continue
                    if vis[vx][vy] or s[vx][vy] != '#': continue
                    vis[vx][vy] = True
                    q.append((vx, vy))
        
    cnt = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] == '#' and vis[i][j] == False:
                bfs(i, j)
                cnt += 1
    print(cnt)

cas = 1
for _ in range(cas):
    solve(_)

