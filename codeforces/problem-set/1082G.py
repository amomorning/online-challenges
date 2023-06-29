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
class Edge:
    def __init__(self, v, next, cap):
        self.v = v
        self.next = next
        self.cap = cap

class MaxFlow:
    s, t = -1, -1
    def __init__(self, n):
        self.n = n
        self.g = []
        self.head = [-1] * self.n

    def add_edge(self, u, v, w):
        self.g.append(Edge(v, self.head[u], w))
        self.head[u] = len(self.g) - 1
        self.g.append(Edge(u, self.head[v], 0))
        self.head[v] = len(self.g) - 1

    def dinic(self, s, t):
        self.s = s
        self.t = t
        flow = 0
        while self.bfs():
            flow += self.dfs(s, math.inf)
        return flow
    
    def get_cuts(self, s, t):
        mark = [False] * self.n
        def remark(u):
            if mark[u]: return
            mark[u] = True
            i = self.head[u]
            while i != -1:
                if self.g[i].cap > 0: remark(self.g[i].v)
                i = self.g[i].next
        remark(s)
        cuts = []
        for u in range(self.n):
            if not mark[u]: continue
            i = self.head[u]
            while i != -1:
                if not mark[self.g[i].v]: 
                    cuts.append((u, self.g[i].v, self.g[i^1].cap))
                i = self.g[i].next
        return cuts


    def bfs(self):
        q = collections.deque([self.t])
        self.dis = [-1] * self.n
        self.cur = [x for x in self.head]
        self.dis[self.t] = self.n
        while q:
            u = q.popleft()
            i = self.head[u]
            while i != -1:
                e = self.g[i]
                if self.g[i^1].cap and self.dis[e.v] == -1:
                    self.dis[e.v] = self.dis[u] - 1
                    q.append(e.v)
                
                i = self.g[i].next
        return self.dis[self.s] != -1
    
    def dfs(self, u, a):
        if u == self.t: return a
        flow, f = 0, 0
        i = self.cur[u]
        while i != -1:
            e = self.g[i]
            if e.cap and self.dis[e.v] > self.dis[u]:
                f = self.dfs(e.v, min(a, e.cap))
                flow += f
                e.cap -= f
                self.g[i^1].cap += f
                a -= f
                if a == 0: break
            i = self.g[i].next
        if flow == 0: self.dis[u] = -1
        return flow

def solve(cas):
    n, m = inp()
    a = inp()
    l = n+m+2
    s, t = 0, l-1
    problem = MaxFlow(l)
    for i in range(n):
        problem.add_edge(s, i+1, a[i])        
    
    sw = 0
    for i in range(n+1, m+n+1):
        u, v, w = inp()
        sw += w
        problem.add_edge(u, i, math.inf)
        problem.add_edge(v, i, math.inf)
        problem.add_edge(i, t, w)
    ans = sw - problem.dinic(s, t)
    print(ans)



cas = 1
for _ in range(cas):
    solve(_)

