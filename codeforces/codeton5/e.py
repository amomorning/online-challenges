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

class LazySegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = make_arr(self.size << 1)(Node)
    
    def build(self, handler):
        self.traverse_all(handler)

    def get_id(self, l, r):
        return l + r | (l != r)
    
    def get_node(self, l, r):
        return self.tree[self.get_id(l, r)]
    

    def traverse_all(self, handler, l=0, r=None):
        if r == None: r = self.size - 1
        if l == r:
            handler(l, r, self.get_node(l, r))
            return
        m = (l+r) >> 1
        lr, lm, mr = self.get_node(l, r), self.get_node(l, m), self.get_node(m+1, r)
        self.down(l, m, r, lr, lm, mr)
        self.traverse_all(handler, l, m)
        self.traverse_all(handler, m+1, r)
        self.up(l, m, r, lr, lm, mr)
    
    def traverse(self, handler, L, R, l=0, r=None):
        if r == None: r = self.size - 1
        if R < l or r < L or L > R: return
        if L <= l and r <= R:
            handler(l, r, self.get_node(l, r))
            return
        m = (l+r) >> 1
        lr, lm, mr = self.get_node(l, r), self.get_node(l, m), self.get_node(m+1, r)
        self.down(l, m, r, lr, lm, mr)
        self.traverse(handler, L, R, l, m)
        self.traverse(handler, L, R, m+1, r)
        self.up(l, m, r, lr, lm, mr)
        
    def query_all(self):
        return self.get_node(0, self.size-1).m

    def query(self, L, R):
        ret = Monoid(True)
        def handler(l, r, u):
            global ret
            ret *= u
        self.traverse(handler, L, R)
        return ret

    def update(self, L, R, dt):
        def handler(l, r, u):
            u.update(dt)
        self.traverse(handler, L, R)
        
    def minify(self, p, val):
        def handler(l, r, u):
            u.m.val = min(u.m.val, val)
        self.traverse(handler, p, p)
    
    def down(self, l, m, r, u, lu, ru):
        if u.tag:
            lu.update(u.tag)
            ru.update(u.tag)
            u.tag = 0
    
    def up(self, l, m, r, u, lu, ru):
        u.m = lu.m * ru.m


class Monoid:
    def __init__(self, id_ = False, val = math.inf):
        self.id_ = id_
        self.val = val
    
    def identity(self):
        return Monoid(True)

    def is_identity(self):
        return self.id_

    def __mul__(self, other):
        if self.is_identity(): return other
        if other.is_identity(): return self
        return Monoid(False, min(self.val, other.val))
    
    def __repr__(self):
        return f'{self.val}'
    
    def __str__(self):
        return f'Monoid::{self.id_} {self.val}'
    
class Node:
    def __init__(self):
        self.m = Monoid()
        self.tag = 0
    
    def update(self, dt):
        if self.m.val == math.inf or dt == 0: return
        self.m.val += dt
        self.tag += dt
    
    def __repr__(self):
        return f'{self.m.val}'
        
ret = Monoid(True)

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
    for _ in range(n):
        x, y, w = inp()
        mp[y].append((x, w))
    seg = LazySegmentTree(k+1)
    u = 0
    for y in range(k, -1, -1):
        for x, w in mp[y]:
            u += w
        seg.update(0, k, a)
        for x, w in mp[y]:
            seg.update(x+1, k, w)
        u = min(u, seg.query_all().val)
        seg.minify(k-y, u)
    print(u)
        

cas = 1
for _ in range(cas):
    solve(_)


