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
MOD = 998244353
def norm(v):
    v = v % MOD
    if v < 0: v += MOD
    return v

class Integral:
    def __init__(self, v):
        self.v = norm(v)

    def __str__(self):
        return str(self.v)
    
    def __neg__(self):
        return Integral(-self.v)

    def __iadd__(self, rhs):
        if type(rhs) == Integral: rhs = rhs.v
        self.v = norm(self.v + rhs)
        return self
    
    def __isub__(self, rhs):
        self += -rhs
        return self
        
    def __imul__(self, rhs):
        if type(rhs) == int: rhs = Integral(rhs)
        self.v = norm(self.v * rhs.v)
        return self
    
    def __itruediv__(self, rhs):
        if type(rhs) == int: rhs = Integral(rhs)
        self.v = norm(self.v * rhs.inv().v)
        return self
    
    def copy(self):
        return Integral(self.v)
    
    def pow(self, b):
        assert type(b) == int
        ret, a = 1, self.v
        while b > 0:
            if b & 1:
                ret = ret * a % MOD
            b >>= 1
            a = a * a % MOD
        return Integral(ret)
    
    def inv(self):
        return self.pow(MOD-2)
    
    def __add__(self, rhs):
        ret = self.copy(); ret += rhs
        return ret

    def __sub__(self, rhs):
        ret = self.copy(); ret -= rhs
        return ret
    
    def __mul__(self, rhs):
        ret = self.copy(); ret *= rhs
        return ret
    
    def __truediv__(self, rhs):
        ret = self.copy(); ret /= rhs
        return ret
    
    def __lshift__(self, rhs):
        if type(rhs) == Integral: rhs = rhs.v
        return Integral(self.v << rhs)

    def __rshift__(self, rhs):
        if type(rhs) == Integral: rhs = rhs.v
        return Integral(self.v >> rhs)
    
    def __pow__(self, rhs):
        return self.pow(rhs)
    
    def __eq__(self, rhs):
        if type(rhs) == Integral: rhs = rhs.v
        return self.v == rhs
    
    def __lt__(self, rhs):
        if type(rhs) == Integral: rhs = rhs.v
        return self.v < rhs
    
    def __le__(self, rhs):
        if type(rhs) == Integral: rhs = rhs.v
        return self.v <= rhs

def solve(cas):
    n, a, b, p, q = inp()
    F = make_arr(n+1, n+1)(lambda: Integral(0))
    G = make_arr(n+1, n+1)(lambda: Integral(0))
    
    for i in range(n, a-1, -1):
        for j in range(n, b-1, -1):
            if i == n and j == n: continue
            if i == n:
                F[i][j] = Integral(1)
                G[i][j] = Integral(1)
                continue
            if j == n:
                F[i][j] = Integral(0)
                G[i][j] = Integral(0)
                continue
            for k in range(1, p+1):
                F[i][j] += G[min(n, i+k)][j]
            F[i][j] /= p
            for k in range(1, q+1):
                G[i][j] += F[i][min(n, j+k)]
            G[i][j] /= q
    print(F[a][b])


cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

