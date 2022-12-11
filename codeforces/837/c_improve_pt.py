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
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0: return False
        return True
    
    def prime_factorization(self, x:int):
        for p in self.primes:
            if p * p > x: break
            if x < len(self.min_div): break
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

class MillerRabin:
    @classmethod
    def pow_mod(self, a, b, mod):
        ans = 1
        while b:
            if b & 1: ans = ans * a % mod
            a = a * a % mod; b >>= 1
        return ans

    @classmethod
    def is_prime(self, n:int):
        if n <= 1: return False
        return not self.miller_rabin(n)

    @classmethod
    def miller_rabin(self, n:int):
        x, t = n-1, 0
        while ~x & 1: 
            x >>= 1 
            t += 1

        flag = True
        if t >= 1 and x & 1:
            cs = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
            for a in cs:
                if self.check_prime(a, n, x, t):
                    flag = True
                    break
                flag = False
        if not flag or n == 2: return False
        return True

    @classmethod
    def check_prime(self, a, n, x, t):
        ret = self.pow_mod(a, x, n)
        last = ret
        for i in range(1, t+1):
            ret = self.pow_mod(ret, 2, n)
            if ret == 1 and last != 1 and last != n-1:
                return True
            last = ret
        if ret != 1: return True
        return False


pt = PrimeTable(1000000)
debug(len(pt.primes))
def solve(cas):
    n, = inp()
    a = inp()
    # l = []
    mp = {}
    for x in a:
        for p, b in pt.prime_factorization(x):
            if p in mp:
                print("YES")
                return
            mp[p] = 1
            # l.append(p)
    print("NO")

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
