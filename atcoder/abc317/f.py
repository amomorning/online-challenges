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
sys.setrecursionlimit(10**6)
# import numpy as np
# import scipy

# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MOD = 998244353

def solve(cas):
    n, a, b, c = inp()
    BIT = 62
    cache = make_arr(BIT, a+1, b+1, c+1, BIT+2)(lambda: 0)
    vis = make_arr(BIT, a+1, b+1, c+1, BIT+2)(lambda: 0)
    
    def dfs(at, x, y, z, bit):
        if at == -1: return int(x == 0 and y == 0 and z == 0)
        # debug(at, x, y, z, lx, ly, lz, rx, ry, rz)
        lx, ly, lz, rx, ry, rz = map(int, list(bin(bit)[2:].zfill(6)))
        if vis[at][x][y][z][bit]: return cache[at][x][y][z][bit]
        vis[at][x][y][z][bit] = 1
        ret = 0
        low = 1 >> at & 1
        high = n >> at & 1
        for i in range(2):
            if lx and i < low: continue
            if rx and i > high: continue
            for j in range(2):
                if ly and j < low: continue
                if ry and j > high: continue
                k = i ^ j
                if lz and k < low: continue
                if rz and k > high: continue
                new_bits = [int(lx and i == low), int(ly and j == low), int(lz and k == low), int(rx and i == high), int(ry and j == high), int(rz and k == high)]
                ret += dfs(at-1, (x*2+i)%a, (y*2+j)%b, (z*2+k)%c, int(''.join(map(str, new_bits)), 2) )
                ret %= MOD
        cache[at][x][y][z][bit] = ret
        return ret
    
    print(dfs(BIT-1, 0, 0, 0, BIT+1))

cas = 1
for _ in range(cas):
    solve(_)

