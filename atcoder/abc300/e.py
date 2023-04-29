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

def crange(start, end, step=1):
    dir = 1 if start < end else -1
    if start > end and step > 0: step = -step
    return range(start, end + dir, step)

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

# binomial
class Binomial:
    def __init__(self, n):
        n = min(n, MOD)
        self.fact = [1, 1]
        self.inv_fact = [1, 1]
        self.inv = [0, 1]
        
        for i in crange(2, n):
            self.fact.append(self.fact[-1] * i % MOD)
            self.inv.append((MOD - MOD // i) * self.inv[MOD % i] % MOD)
            self.inv_fact.append(self.inv_fact[-1] * self.inv[-1] % MOD)
    

    def comb(self, n, m):
        if m < 0 or m > n:
            return 0
        m = min(m, n-m)
        return self.fact[n] * self.inv_fact[m] * self.inv_fact[n-m] % MOD

    ''' Lucas theorem
    - mod should be less than 1e5
    '''
    def lucas(self, n, m): 
        if m == 0:
            return 1
        return self.comb(n % MOD, m % MOD) * \
            self.lucas(n // MOD, m // MOD) % MOD


def solve(cas):
    n, = inp()
    a, b, c = 0, 0, 0
    
    while n % 2 == 0: 
        n //= 2
        a += 1
    while n % 3 == 0:
        n //= 3
        b += 1
    while n % 5 == 0:
        n //= 5
        c += 1
    
    if n > 1:
        print(0)
        return
    
    ans = Integral(0)
    bino = Binomial(60)
    for x in range(a//2+1):
        for y in range(min(a-x*2, b)+1):
            aa = a-x*2-y
            bb = b-y
            # print(aa, bb, c, x, y)
            tmp = norm(bino.fact[aa+bb+c+x+y] * bino.inv_fact[aa] * bino.inv_fact[bb] * bino.inv_fact[c] * bino.inv_fact[x] * bino.inv_fact[y])
            ans += Integral(tmp) / Integral(5).pow(aa+bb+c+x+y)
    print(ans.v)
            
            


cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

