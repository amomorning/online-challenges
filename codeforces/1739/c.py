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
def crange(start, end, step=1):
    dir = 1 if start < end else -1
    if start > end and step > 0: step = -step
    return range(start, end + dir, step)
# binomial
MOD = 998244353
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


MAX = 31
a, b = [0] * MAX, [0] * MAX
bino = Binomial(MAX*2)
for i in range(1, MAX):
    debug(i*2-1, i)
    tot = bino.comb(i*2, i)
    a[i] = (b[i-1] + bino.comb(i*2-1, i-1))%MOD
    b[i] = (tot - a[i] - 1+MOD)%MOD
    

def solve(cas):
    n = int(input())
    print(a[n//2], b[n//2], 1)
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
