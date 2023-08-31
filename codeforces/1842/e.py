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

class ZKWSegmentTree: 
    def __init__(self, n): 
        self.size =  1 << (n+2).bit_length() 
        self.tree = [0] * (self.size*2)
    def update(self, l, r, x):
        tree, n = self.tree, self.size 
        if l <= 0:
            r += n+1
            while r > 1 :
                if r & 1:  tree[r ^ 1] += x
                tmp = max(tree[r], tree[r ^ 1])
                tree[r] -= tmp;tree[r ^ 1] -= tmp;tree[r >> 1] += tmp
                r >>= 1 
        elif r>=n-1:
            l += n-1
            while l > 1 :
                if ~l & 1: tree[l ^ 1] += x
                tmp = max(tree[l], tree[l ^ 1])
                tree[l] -= tmp;tree[l ^ 1] -= tmp;tree[l >> 1] += tmp
                l >>= 1
        elif l == r:
            tree, n = self.tree, self.size 
            l += n 
            tree[l] += x 
            while l > 1 :
                tmp = max(tree[l], tree[l ^ 1])
                tree[l] -= tmp;tree[l ^ 1] -= tmp;tree[l >> 1] += tmp
                l >>= 1
        elif l < r:
            l += n-1
            r += n+1
            while l ^ r ^ 1:
                if ~l & 1: tree[l ^ 1] += x
                if r & 1:  tree[r ^ 1] += x
                tmp = max(tree[l], tree[l ^ 1])
                tree[l] -= tmp;tree[l ^ 1] -= tmp;tree[l >> 1] += tmp
                tmp = max(tree[r], tree[r ^ 1])
                tree[r] -= tmp;tree[r ^ 1] -= tmp;tree[r >> 1] += tmp
                l >>= 1;r >>= 1
            while l > 1 :
                tmp = max(tree[l], tree[l ^ 1])
                tree[l] -= tmp;tree[l ^ 1] -= tmp;tree[l >> 1] += tmp
                l >>= 1
    
    def query_all(self):
        return self.query(0, self.size-1)

    def query(self, l, r):
        tree = self.tree
        l += self.size 
        r += self.size 
        S = T = 0
        if l ^ r : 
            while l ^ r ^ 1:
                S += tree[l] ; T += tree[r]
                if ~l & 1 : S = max(S,tree[l^1])
                if r & 1  : T = max(T,tree[r^1])
                l >>= 1 ; r >>= 1 
        S = max(tree[l]+S,tree[r]+T) 
        while l > 1: 
            l >>= 1 ; S += tree[l]
        return S


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

def solve(cas):
    n, k, a = inp()
    mp = Encodict(list)
    s = 0
    for _ in range(n):
        x, y, w = inp()
        mp[y].append((x, w))
        s += w
    seg = ZKWSegmentTree(k+1)
    u = 0
    for y in range(k, -1, -1):

        for x, w in mp[y]:
            seg.update(0, x, w)
        u = max(u, seg.query_all() - a*(k-y))
        seg.update(k-y, k-y, u+(k-y)*a)
    print(s-u)
        

cas = 1
for _ in range(cas):
    solve(_)


