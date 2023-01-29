#!/usr/bin/env python3
import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
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

def solve(cas):
    n, = inp()
    a = inp()
    iv = set()
    mp = Encodict(set) 
    f = [[] for _ in range(n)]
    sink = set()
    first = set()
    u = 0
    flag = -1
    while u < n and u >= 0:
        first.add(u)
        if a[u]+u in first:
            flag = u
            break
        u = a[u] + u
    
    for i in range(n):
        u = i + a[i]
        if a[i] == 0:
            sink.add(i)
        elif u >= 0 and u < n:
            f[u].append(i)

    for i in range(n):
        if i+a[i] < 0 or i+a[i] >= n:
            q = collections.deque([i])
            while q:
                u = q.popleft()
                iv.add(u)
                for v in f[u]:
                    if v not in iv:
                        q.append(v)
    
    for i in range(n):
        q = collections.deque([i])
        while q:
            u = q.popleft()
            mp[i].add(u)
            for v in f[u]:
                if v not in mp[i]:
                    q.append(v)
            
    # debug(first)
    # debug(iv)
    debug(flag)
    ans = 0
    if flag != -1:
        for x in first:
            ans += (n+1)
            ans += len(iv - mp[flag] - sink)
    else:
        for i in range(n):
            if i not in first:
                ans += 2*n+1
            else:
                ans += (n+1)
                # debug(iv-mp[i]-sink)
                ans += len(iv-mp[i]-sink)
    print(ans)


cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)
