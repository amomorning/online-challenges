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
        return self.get_node(0, self.size-1)

    def query(self, L, R):
        self.ret = [0, 0]
        def handler(l, r, u):
            self.ret[0] ^= u.l
            self.ret[1] ^= u.r
        self.traverse(handler, L, R)
        return self.ret

    def up(self, l, m, r, u, lu, ru):
        u.l = lu.l ^ ru.l
        u.r = lu.r ^ ru.r

    def update(self, L, R):
        def handler(l, r, u):
            u.update()
        self.traverse(handler, L, R)
    
    def down(self, l, m, r, u, lu, ru):
        if u.tag > 0:
            lu.update()
            ru.update()
            u.tag = 0
    

    
    
class Node:
    def __init__(self):
        self.tag = 0
        self.l = 0
        self.r = 0
    
    def update(self):
        self.l, self.r = self.r, self.l
        self.tag ^= 1


def solve(cas):
    n, = inp()
    a = inp()
    s = input()
    lsg = LazySegmentTree(n)
    def handler(l, r, u):
        assert l==r
        if s[l] == '0':
            u.l = a[l]
        else:
            u.r = a[l]
    lsg.build(handler)
    ans = []
    for _ in range(int(input())):
        op, *q = inp()
        if op == 2:
            if q[0] == 0:
                ans.append(lsg.query_all().l)
            else:
                ans.append(lsg.query_all().r)
        else:
            l, r = q
            lsg.update(l-1, r-1)
    printf(ans)





cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

