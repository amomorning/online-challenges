import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))
sys.setrecursionlimit(10**6)
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
    def __init__(self, n):
        self.uf = list(range(n))
        self.p = list(range(n))
        self.id = list(range(n))
    
    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]
    
    def union(self, x, y):
        if self.id[y] == -1:
            return
        if self.id[x] == -1:
            self.id[x] = self.id[y]
            self.p[self.id[x]] = x
        else:
            self.uf[self.id[y]] = self.id[x]
        self.id[y] = -1
    
    

def solve(cas):
    n, q = inp()
    cur = n
    uf = UnionFind(n+q)
    for _ in range(q):
        op = inp(lambda x: int(x)-1)
        if op[0] == 0:
            uf.union(op[1], op[2])
        if op[0] == 1:
            uf.union(op[1], cur)
            cur += 1
        if op[0] == 2:
            print(uf.p[uf.find(op[1])] + 1)

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

cas = 1
for _ in range(cas):
    solve(cas)
