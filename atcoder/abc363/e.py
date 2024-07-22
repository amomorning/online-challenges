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


d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

class Encodict:
    def __init__(self, func=lambda : 0):
        self.RANDOM = random.randint(0, 1<<32)
        self.default = func
        self.dict = {}
    
    def __getitem__(self, key):
        k = self.RANDOM ^ key
        if k not in self.dict:
            self.dict[k] = self.default()
        return self.dict[k]
    
    def __setitem__(self, key, item):
        k = self.RANDOM ^ key
        self.dict[k] = item

    def keys(self):
        return [self.RANDOM ^ i for i in self.dict]
    
    def items(self):
        return [(self.RANDOM ^ i, self.dict[i]) for i in self.dict]
    
    def sorted(self, by_value=False, reverse=False):
        if by_value:
            self.dict = dict(sorted(self.dict.items(), \
                key=lambda x:x[1], reverse=reverse))
        else:
            self.dict = dict(sorted(self.dict.items(), \
                key=lambda x:self.RANDOM^x[0], reverse=reverse))

class UnionFind:
    def __init__(self, x) -> None:
        self.uf = [-1] * x
        self.weight = [0] * x
 
    def find(self, x):
        r = x
        while self.uf[x] >= 0:
            x = self.uf[x]
        while r != x:
            self.uf[r], r = x, self.uf[r]
        return x
 
    def same(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return False
        self.uf[y] = x
        self.weight[x] += self.weight[y]
        return True


def solve(cas):
    H, W, Y = inp()
    A = [inp() for _ in range(H)]
    bucket = Encodict(list)
    for i in range(H):
        for j in range(W):
            if A[i][j] > Y: continue
            bucket[A[i][j]].append((i, j))
    
    dsu = UnionFind(H*W+1)
    
    for y in range(1, Y+1):
        for i, j in bucket[y]:
            dsu.weight[i*W+j] += 1
            for dx, dy in d4:
                ni, nj = i+dx, j+dy
                if ni < 0 or nj < 0 or ni >= H or nj >= W:
                    dsu.merge(i*W+j, H*W)
                    continue
                v = dsu.find(ni*W+nj)
                if dsu.weight[v] == 0: continue
                dsu.merge(i*W+j, ni*W+nj)

        z = dsu.find(H*W)
        print(H*W-dsu.weight[z])

                


cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

