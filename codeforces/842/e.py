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

MOD = 998244353
def crange(start, end, step=1):
    dir = 1 if start < end else -1
    if start > end and step > 0: step = -step
    return range(start, end + dir, step)

def norm(v):
    v = v % MOD
    if v < 0: v += MOD
    return v

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
    global MOD
    n, MOD = inp()

    bino = Binomial(n*3)
    F = [0] * 4
    F[0] = 1
    F[1] = norm(bino.fact[n*2] * 2 - bino.fact[n])
    for i in range(n+1):
        F[2] += norm(bino.comb(n, i) ** 2) \
            * (-bino.comb(n*2-i, n) + bino.comb(n*2, n) * 2)
        F[2] = norm(F[2])
    F[2] *= norm(bino.fact[n] ** 3)
    F[2] = norm(F[2])
    F[3] = bino.fact[n * 3]
 
    F[3] -= F[2]
    F[2] -= F[1]
    F[1] -= F[0]

    ans = 0
    for i in range(4):
        ans += F[i] * i
        ans = norm(ans)
    print(ans)


cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
