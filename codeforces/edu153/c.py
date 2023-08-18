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

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bits = [0] * n
    
    def ask(self, p, tot=0):
        while p >= 0: tot = max(tot, self.bits[p]); p -= ~p & p + 1
        return tot
    
    def add(self, p, x):
        while p < self.n: 
            self.bits[p] = max(self.bits[p], x)
            p += ~p & p + 1

    ''' k in [1, n]
    '''
    def kth(self, k):
        p, t = -1, 0
        b = self.n.bit_length()
        while ~b:
            p += 1 << b
            if p >= self.n or t + self.bits[p] >= k: 
                p -= 1 << b
            else:
                t += self.bits[p]
            b -= 1
        return -1 if p+1 >= self.n else p + 1

def solve(cas):
    n, = inp()
    a = inp(lambda x: int(x)-1)
    f = Fenwick(n)
    dp = [0] * n
    for i in range(n):
        tmp = f.ask(a[i])
        dp[i] = tmp+1
        f.add(a[i], tmp+1)
    debug(dp)
    print(dp.count(2))
    

    


cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

