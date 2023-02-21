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

class Tree:
    def __init__(self, n):
        self.size = [1] * n
        self.mx = [-1] * n
        self.p = [-1] * n
        self.G = Encodict(list)
        self.n = n
        
    def dfs(self, root):
        self.topo = []
        q = collections.deque([root])
        while q:
            u = q.popleft()
            self.topo.append(u)
            
            for v in self.G[u]:
                if self.p[v] == -1 and v != root:
                    self.p[v] = u
                    q.append(v)
        self.topo = self.topo[::-1]

    def calc(self):
        for u in self.topo:
            mx = -1
            for v in self.G[u]:
                if v != self.p[u]:
                    self.size[u] += self.size[v]
                mx = max(mx, self.size[v])
            self.mx[u] = max(mx, self.n - self.size[u])
    
    def find_leaf(self, u, p):
        pa = [-1] * self.n
        q = collections.deque([u])
        pa[u] = p
        while q:
            u = q.popleft()
            tot = 0
            for v in self.G[u]:
                if v == pa[u]: continue
                pa[v] = u
                tot += 1
                q.append(v)
            if tot == 0:
                return u

def solve(cas):
    n, = inp()
    tree = Tree(n)
    for i in range(n-1):
        u, v = inp(lambda x: int(x)-1)
        tree.G[u].append(v)
        tree.G[v].append(u)
    tree.dfs(0)
    tree.calc()
    mn = min(tree.mx)
    centers = [i for i in range(n) if tree.mx[i] == mn]
    if len(centers) == 1:
        print(1, tree.G[0][0]+1)
        print(1, tree.G[0][0]+1)
    else:
        a = tree.find_leaf(*centers)
        b = tree.G[a][0]
        c = centers[1]
        print(a+1, b+1)
        print(a+1, c+1)
        

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

