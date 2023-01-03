import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
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
        self.uf[uy] = ux
        return True
        # if self.uf[ux] >= self.uf[uy]:
        #     self.uf[uy] += self.uf[ux]
        #     self.uf[ux] = uy
        # else:
        #     self.uf[ux] += self.uf[uy]
        #     self.uf[uy] = ux
        # return True
 
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

def group(arr):
    cnt = Encodict(lambda : 0)
    for a in arr:
        cnt[a] += 1
    return cnt.items()
        

def solve(cas):
    n, = inp()
    a, b = inp(), inp()
    m, = inp()
    x = group(sorted(inp()))
            
    mp = Encodict(list)
    uf = UnionFind(n)
    for i in range(n):
        if a[i] < b[i]:
            print("NO")
            return
        mp[b[i]].append(i)
    
    mark = Encodict(lambda : 0)
    
    for xx, num in x:
        cur = set()
        for p in mp[xx]:
            if p > 0 and b[p-1] <= b[p]:
                uf.union(p-1, p)
            if p+1 < n and b[p+1] <= b[p]:
                uf.union(p, p+1)
            cur.add(uf.find(p))
        debug('cur =', cur, 'x =', xx)
        if len(cur) > num:
            print("NO")
            return
        mark[xx] = 1
    
    for i in range(n):
        if mark[b[i]] == 1: continue
        if b[i] != a[i]:
            print("NO")
            return
   
    debug('-------------')
    print("YES")


        

                

        

        
    
    


cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
