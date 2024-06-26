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


from types import GeneratorType
def bootstrap(f, stack=None):
    if stack is None:
        stack = []
 
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
 
    return wrappedfunc


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


class Tarjan:
    """ 
    Parameters:
    ----------
    n: int
        number of nodes
    
    Usage:
    ----------
    ```
    tarjan = Tarjan(n)

    tarjan.add_edge(u, v)

    for i in range(n):
        if tarjan.dfn[i] == -1:
            tarjan.bcc.append([])
            tarjan.tarjan(i, -1)
    
    for bcc in tarjan.bcc:
        for u in bcc:
            if tarjan.is_cut[u]:
    ```
    """
    def __init__(self, n):
        self.n = n
        self.g = Encodict(list)
        self.low = [-1] * n # the lowest order
        self.dfn = [-1] * n # dfs number - the order of the node being visited
        self.par = [-1] * n # parent of u
        self.size = [0] * n # size of the subtree rooted at u
        self.is_cut = [False] * n # is (u, par[u]) a cut edge
        self.clock = 0
        self.bcc = [] # connected components, bcc.append([]) to add a new component
    
    @bootstrap
    def tarjan(self, u, fa):
        self.bcc[-1].append(u)
        self.par[u] = fa
        self.low[u] = self.dfn[u] = self.clock
        self.clock += 1

        for v in self.g[u]:
            if self.dfn[v] == -1:
                yield self.tarjan(v, u)
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] > self.dfn[u]:
                    self.is_cut[v] = True
            elif v != fa and self.dfn[v] < self.dfn[u]:
                self.low[u] = min(self.low[u], self.dfn[v])
        self.size[u] = self.clock - self.low[u]
        yield
    
    def add_edge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def solve(cas):
    global g, low, dfn, scc
    n, m = inp()
    tarjan = Tarjan(n)

    for _ in range(m):
        u, v = inp()
        u -= 1; v -= 1
        tarjan.add_edge(u, v)

    for i in range(n):
        if tarjan.dfn[i] == -1:
            tarjan.bcc.append([])
            tarjan.tarjan(i, -1)
  
    tot, res = 0, 0
    for bcc in tarjan.bcc:
        n = len(bcc)
        tot += n * (n-1) // 2
        for u in bcc:
            if tarjan.is_cut[u]:
                sz = tarjan.size[u]
                res = max(res, sz * (n-sz))
    print(tot - res)


cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

