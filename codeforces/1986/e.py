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
    n, K = inp()
    a = inp()
    if K == 1:
        a = sorted(a)
        if len(a) % 2 == 0:
            ans = 0
            for i in range(1, n):
                if i % 2 == 1:
                    ans += abs(a[i] - a[i-1])
            print(ans)
            return
        s = make_arr(n+1)(lambda: 0)
        for i in range(n-2, -1, -1):
            s[i] = a[i+1] - a[i] + s[i+2]
        # debug(s)
        ans = 10**18
        for i in range(n):
            if i % 2 == 0:
                ans = min(ans, s[i+1]+s[0]-s[i])
        print(ans)
    else:
        d = Encodict(list)
        for x in a:
            d[x%K].append(x)
        
        cnt_odd = 0
        ans = 0
        for k in d.keys():
            d[k].sort()
            if len(d[k]) % 2 == 1:
                cnt_odd += 1
                s = make_arr(len(d[k])+1)(lambda: 0)
                for i in range(len(d[k])-2, -1, -1):
                    s[i] = d[k][i+1] - d[k][i] + s[i+2]
                # debug(s)
                mn = 10**18
                for i in range(len(d[k])):
                    if i % 2 == 0:
                        mn = min(mn, s[i+1]+s[0]-s[i])
                ans += mn//K
            else:
                for i in range(0, len(d[k]), 2):
                    ans += (d[k][i+1] - d[k][i]) // K

        if cnt_odd > 1:
            print(-1)
            return
        print(ans)

        


                




cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

