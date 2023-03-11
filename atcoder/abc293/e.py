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

# avaliable on Google, AtCoder
# sys.setrecursionlimit(10**6)
# import numpy as np
# import scipy

# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def exgcd(a, b):
    x = [1, 0, 0, 1]
    while b != 0:
        c = a // b
        x, a, b = [x[2], x[3], x[0] - x[2] * c, x[1] - x[3] * c], b, a % b
    return a, x[0], x[1]

MOD = 998244353
def norm(v):
    global MOD
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
        global MOD
        assert type(b) == int
        ret, a = 1, self.v
        while b > 0:
            if b & 1:
                ret = ret * a % MOD
            b >>= 1
            a = a * a % MOD
        return Integral(ret)
    
    def inv(self):
        global MOD
        gcd, x, _ = exgcd(self.v, MOD)
        return Integral(norm(x))
    
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


def linear_diophantine(a, b, c):
    """ Solution for ax + by = c
        return: gcd(a, b), x, y
    """
    if a == 0 and b == 0: return 0, 0, 0 if c == 0 else False
    if a == 0: return abs(b), 0, c//b if c%b == 0 else False
    if b == 0: return abs(a), c//a, 0 if c%a == 0 else False
    d, x, y = exgcd(a, b)
    if c % d != 0: return False
    dx = c // a; c -= dx * a
    dy = c // b; c -= dy * b
    x = dx + x * (c // d) % b
    y = dy + y * (c // d) % a
    return abs(d), x, y


def linear_congruence(k1, m1, k2, m2):
    """ Solution for x = k1(mod m1)
                     x = k2(mod m2)			   
        return: x, lcm(m1, m2)  (0 <= x < lcm(m1, m2))
    """
    k1 %= m1; k2 %= m2
    if k1 < 0: k1 += m1
    if k2 < 0: k2 += m2

    tmp = linear_diophantine(m1, -m2, k2-k1)
    if tmp == False: return False
    
    d, x, _ = tmp
    dx = m2 // d
    delta = x // dx - int(x % dx < 0)
    return m1 * (x - dx * delta) + k1, m1 // d * m2


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

pt = PrimeTable(1000000)

def calc(a, x, p, w):
    global MOD
    if w == 1: return 0
    if a % w == 0: return 1
    if math.gcd(a-1, w) == 1:
        MOD = w
        aa = Integral(a)
        return norm(((aa.pow(x) - 1) / (a-1)).v)
    t, r = 0, a-1
    while r % p == 0:
        r //= p
        t += 1
    MOD = w * int(math.pow(p, t))
    aa = Integral(a)
    tmp = (aa.pow(x) - 1).v // int(math.pow(p, t))
    MOD = w
    return tmp * Integral(r).inv().v % MOD

def solve(cas):
    global MOD
    a, x, m = inp()
    if a == 1:
        print(x%m)
        return
    
    u, v = 0, 1
    for p, b in pt.prime_factorization(m):    
        w = int(math.pow(p, b))
        u, v = linear_congruence(u, v, calc(a, x, p, w), w)
        
    print(u)

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

