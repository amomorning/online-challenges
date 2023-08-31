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

def check(H, W, a):
    vis = [0] * len(a)
    h = Encodict(list)
    w = Encodict(list)
    
    for i, (x, y) in enumerate(a):
        h[x].append(i)
        w[y].append(i)
    
    while H > 0 and W > 0:
        flag = False
        for i in h[H]:
            if vis[i] == 1: continue
            W -= a[i][1]
            flag = True
            vis[i] = 1
        for i in w[W]:
            if vis[i] == 1: continue
            H -= a[i][0]
            flag = True
            vis[i] = 1
        if not flag: return False
    return True
    

def solve(cas):
    n, = inp()
    a = [tuple(inp()) for _ in range(n)]
    tot = sum([x[0]*x[1] for x in a])
    mxh = max(a, key=lambda x: x[0])[0]
    mxw = max(a, key=lambda x: x[1])[1]
    ans = set()
    if tot % mxh == 0:
        if check(mxh, tot//mxh, a):
            ans.add((mxh, tot//mxh))
    if tot % mxw == 0:
        if check(tot//mxw, mxw, a):
            ans.add((tot//mxw, mxw))
    print(len(ans))
    for h, w in ans:
        print(h, w)


cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

