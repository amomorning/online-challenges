import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda : list(map(int, input().split()))

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

def bit_count(x):
    return bin(x).count('1')

N, M = inp()
X = inp()
Y = inp()
edges = []
G = [[] for _ in range(N)]
for i in range(M):
    A, B, Z = inp()
    A -= 1; B -= 1
    edges.append((Z, A, B))

ans = math.inf
for t in range(4):
    es = copy.copy(edges)
    for i in range(N):
        if t&1: es.append((X[i], i, N))
        if t&2: 
            es.append((Y[i], i, N + bit_count(t)-1))

    
    # print(es)
    uf = UnionFind(N + bit_count(t))

    es = sorted(es, key=lambda x: x[0])
    tot, num = 0, 0
    for w, u, v in es:
        if uf.same(u, v): continue
        tot += w
        num += 1
        uf.union(u, v)
    if num == N + bit_count(t) - 1:
        ans = min(ans, tot)

print(ans)
