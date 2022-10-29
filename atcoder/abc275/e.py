import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


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

    def __repr__(self):
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
    n, m, k = inp()
    dp = [[Integral(0) for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = Integral(1)
    for t in range(1, k+1):
        for i in range(n):
            if dp[i][t-1] == 0: continue
            for j in range(1, m+1):
                tmp = i+j if i+j <= n else 2*n-i-j
                dp[tmp][t] += dp[i][t-1] / m
    
    tot = Integral(0)
    for t in range(1, k+1):
        tot += dp[n][t]
    print(tot)
    

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
