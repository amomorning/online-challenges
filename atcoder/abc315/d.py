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
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
tmp = dict(zip('abcdefghijklmnopqrstuvwxyz', range(26)))

def num(arr):
    return 26 - arr.count(0)

def solve(cas):
    h, w = inp()
    s = [input() for _ in range(h)]
    rows = [[0] * 26 for _ in range(h)]
    cols = [[0] * 26 for _ in range(w)]
    rr, cc = [0] * h, [0] * w
    rw, cw = [0] * h, [0] * w
    
    for i in range(h):
        for j in range(w):
            if rows[i][tmp[s[i][j]]] == 0: rr[i] += 1
            if cols[j][tmp[s[i][j]]] == 0: cc[j] += 1
            rows[i][tmp[s[i][j]]] += 1
            cols[j][tmp[s[i][j]]] += 1
            rw[i] += 1
            cw[j] += 1
    debug(rr)
    
            
    
    while True:
        mkr, mkc = [], []
        

        for i in range(h):
            if rr[i] == 1 and rw[i] != 1:
                mkr.append(i)
        for j in range(w):
            if cc[j] == 1 and cw[j] != 1:
                mkc.append(j)

        if mkr or mkc:
            debug(mkr)
            debug(mkc)
            for j in range(w):
                for i in mkr:
                    ch = tmp[s[i][j]]
                    if rows[i][ch] > 0:
                        rows[i][ch] -= 1

                    if cw[j] > 0:
                        cols[j][ch] -= 1
                        cw[j] -= 1
                    if cols[j][ch] == 0:
                        cc[j] -= 1

                
            for i in range(h):
                for j in mkc:
                    ch = tmp[s[i][j]]
                    if cols[j][ch] > 0:
                        cols[j][ch] -= 1

                    if rw[i] > 0:
                        rows[i][ch] -= 1
                        rw[i] -= 1
                    if rows[i][ch] == 0:
                        rr[i] -= 1

            for i in mkr:
                rr[i] = 0
                rw[i] = 0
            
            for j in mkc:
                cc[j] = 0
                cw[j] = 0
            
            debug('cw', cw)
            debug('cc', cc)
            debug('rw', rw)
            debug('rr', rr)
        else:
            break
    
    print(sum(cw[i] for i in range(w)))
        

cas = 1
for _ in range(cas):
    solve(_)

