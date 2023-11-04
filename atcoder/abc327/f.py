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
        self.ret = 0
        def handler(l, r, u):
            self.ret = max(self.ret, u.m)
        self.traverse(handler, L, R)
        return self.ret

    def up(self, l, m, r, u, lu, ru):
        u.m = max(lu.m , ru.m)

    def update(self, L, R, dt):
        def handler(l, r, u):
            u.update(l, r, dt)
        self.traverse(handler, L, R)
    
    def down(self, l, m, r, u, lu, ru):
        if u.tag != 0:
            lu.update(l, m, u.tag)
            ru.update(m+1, r, u.tag)
            u.tag = 0
    

    
class Node:
    def __init__(self):
        self.m = 0
        self.tag = 0
    
    def update(self, l, r, dt):
        self.m += dt
        self.tag += dt
    
    def __repr__(self):
        return f'{self.m.val}'


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

# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def solve(cas):
    N, D, W = inp()
    coords = Encodict(list)
    MAX, MAXV = 0, 0
    for i in range(N):
        u, v = inp()
        MAX = max(MAX, u)
        MAXV = max(MAXV, v)
        coords[u].append(v)

    tree = LazySegmentTree(MAXV)

    for i in range(D):
        for v in coords[i]:
            tree.apply(v-W+1, v, 1)

    ans = tree.query_all()
    for i in range(D, MAX+1):
        for v in coords[i-D]:
            tree.apply(v-W+1, v, -1)
        for v in coords[i]:
            tree.apply(v-W+1, v, 1)
        ans = max(ans, tree.all_prod())
    print(ans)
    
    

cas = 1
for _ in range(cas):
    solve(_)

