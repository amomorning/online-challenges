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

def toposort(G, topo=[]):
    d = [0] * len(G)
    for vs in G:
        for v in vs:
            d[v] += 1
    q = collections.deque([u for u, du in enumerate(d) if du == 0])
    while q:
        u = q.popleft()
        topo.append(u)
        for v in G[u]:
            d[v] -= 1
            if d[v] == 0:
                q.append(v)
    if sum(d):
        return False
    return True

def solve(cas):
    n, m, k = inp()
    h = inp()
    G = [[] for _ in range(n)]
    P = [[] for _ in range(n)]
    lim = [[0, math.inf] for _ in range(n)]

    for _ in range(m):
        u, v = inp(lambda x: int(x)-1)
        G[u].append(v)
        P[v].append(u)
    topo = []
    toposort(G, topo)

    def update(s, value):
        q = collections.deque([s])
        while q:
            u = q.popleft()
            for v in P[u]:
                if lim[v][1] > value:
                    lim[v][1] = value
                    q.append(v)
    
    debug(topo)
    for i in range(n):
        u = topo[i]
        for p in P[u]:
            lim[u][0] = max(lim[u][0], lim[p][0])
            if h[u] < h[p]:
                debug(u, p, lim[u][0], lim[p][0])
                lim[u][0] = max(lim[u][0], lim[p][0] + 1)
                debug(u, p, lim[u][0], lim[p][0])
                lim[p][1] = lim[p][0]
                update(p, lim[p][0])
    
    # debug(lim)
    mn = math.inf
    mx = [max([l for l, r in lim]), 0]
    for i in range(n):
        if lim[i][0] == 0 and lim[i][1] == 0:
            mn = min(mn, h[i])
        if lim[i][0] == mx[0]:
            mx[1] = max(mx[1], h[i])
    
    debug(lim)
    notin = []
    for i in range(n):
        if lim[i][0] == 0 and h[i] < mn:
            if mx[0] == 1 and mx[1] < h[i]:
                notin.append(h[i])
    debug(notin)
    
    if notin:
        if mn - min(notin) <= max(notin) - mx[1]:
            mn = min(notin)
        else:
            mx[1] = max(notin)
    

    ans = math.inf
    if mn == math.inf:
        a = sorted(h)
        if a[0] == a[-1]: ans = min(ans, 0)
        for i in range(n):
            if a[i-1] > a[i]:
                ans = min(ans, a[i-1]-a[i])
            else:
                ans = min(ans, k-a[i] + a[i-1])
    else:
        ans = k-mn + (mx[0]-1) * k + mx[1]
        debug(mn, '-', mx)
    print(ans)


        
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

