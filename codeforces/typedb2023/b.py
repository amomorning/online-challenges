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
import math
class PrimeTable:
    def __init__(self, n:int) -> None:
        self.n = n

        self.primes = []
        self.min_div = [0] * (n+1)
        self.min_div[1] = 1

        mu = [0] * (n+1)
        phi = [0] * (n+1)
        mu[1] = 1
        phi[1] = 1

        for i in range(2, n+1):
            if not self.min_div[i]:
                self.primes.append(i)
                self.min_div[i] = i
                mu[i] = -1
                phi[i] = i-1
            for p in self.primes:
                if i * p > n: break
                self.min_div[i*p] = p
                if i % p == 0:
                    phi[i*p] = phi[i] * p
                    break
                else:
                    mu[i*p] = -mu[i]
                    phi[i*p] = phi[i] * (p - 1)

    def is_prime(self, x:int):
        if x < 2: return False
        if x <= self.n: return self.min_div[x] == x
        for p in self.primes:
            if p * p > x: break
            if x % p == 0: return False
        for i in range(self.n+1, int(math.sqrt(x))+1):
            if x % i == 0: return False
        return True
    
    def prime_factorization(self, x:int):
        for p in self.primes:
            if p * p > x or x <= self.n: break
            if x % p == 0:
                cnt = 0
                while x % p == 0: 
                    cnt += 1
                    x //= p
                yield p, cnt
        for p in range(len(self.min_div), int(math.sqrt(x))+1):
            if x <= self.n: break
            if x % p == 0:
                cnt = 0
                while x % p == 0: cnt += 1; x //= p
                yield p, cnt
        while (1 < x and x <= self.n):
            p, cnt = self.min_div[x], 0
            while x % p == 0: cnt += 1; x //= p
            yield p, cnt
        if x >= self.n and x > 1:
            yield x, 1
    
    def get_factors(self, x:int):
        """ Not in ascending order"""
        factors = [1]
        for p, b in self.prime_factorization(x):
            n = len(factors)
            for j in range(1, b+1):
                for d in factors[:n]:
                    factors.append(d * (p ** j))
        return factors

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

pt = PrimeTable(100000)

def solve(cas):
    n, = inp()
    mp = Encodict()
    bs = set()
    for p, b in pt.prime_factorization(n):
        mp[p] = b
        bs.add(b)
    
    bs = sorted(bs)
    cur = 0
    ans = 0
    for b in bs:
        tot = 1
        for p in mp.keys():
            if mp[p] >= b:
                tot *= p
        ans += tot * (b-cur)
        cur = b
    print(ans)
        
        
            

        
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
