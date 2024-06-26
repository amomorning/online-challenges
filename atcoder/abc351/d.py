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


class UnionFind:
    def __init__(self, x) -> None:
        self.uf = [-1] * x
 
    def find(self, x):
        r = x
        while self.uf[x] >= 0:
            x = self.uf[x]
        while r != x:
            self.uf[r], r = x, self.uf[r]
        return x
 
    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        ux, uy = self.find(x), self.find(y)
        if ux == uy:
            return False
        if self.uf[ux] >= self.uf[uy]:
            self.uf[uy] += self.uf[ux]
            self.uf[ux] = uy
        else:
            self.uf[ux] += self.uf[uy]
            self.uf[uy] = ux
        return True
 
    def count(self):
        return sum(f < 0 for f in self.uf)
 
    def valid(self):
        n = len(self.uf)
        for c in range(n):
            if self.uf[c] == -n:
                return True
        return False
    
    def roots(self):
        return [i for i, f in enumerate(self.uf) if f < 0]

    def groups(self):
        n = len(self.uf)
        ret = [[] for _ in range(n)]
        for i in range(n):
            f = self.find(i)
            ret[f].append(i)
        return ret
 
    def __print__(self):
        return self.uf

d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def solve(cas):
    n, m = inp()
    s = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if s[i][j] == '#':
                for dx, dy in d4:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < n and 0 <= nj < m and s[ni][nj] == '.':
                        s[ni][nj] = '-'
    
    uf = UnionFind(n*m)
    st = set()
    for i in range(n):
        for j in range(m):
            if s[i][j] == '.':
                for dx, dy in d4:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < n and 0 <= nj < m and s[ni][nj] == '.':
                        uf.union(i*m+j, ni*m+nj)
                    

    res = 1
    for ug in uf.groups():
        ans = set(ug)
        flag = True
        for i in ug:
            if s[i//m][i%m] != '.': continue

            for dx, dy in d4:
                ni, nj = i//m+dx, i%m+dy
                if 0 <= ni < n and 0 <= nj < m and s[ni][nj] == '-':
                    ans.add(ni*m+nj)
        res = max(res, len(ans))
    print(res)
        


    



cas = 1
for _ in range(cas):
    solve(_)

