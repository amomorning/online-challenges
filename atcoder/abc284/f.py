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

class Hash:
    def __init__(self, s, seed=214131331, mod=9898798161):
        self.n = len(s)
        self.pw = [1]
        self.mod = mod
        self.table = [0] * (self.n + 1)

        for i in range(1, self.n):
            self.pw.append(self.pw[-1] * seed % mod)
        
        for i in range(self.n-1, -1, -1):
            self.table[i] = self.table[i+1] * seed + ord(s[i])
            self.table[i] %= mod

    def get(self, l, r):
        return (self.table[l] - self.table[r+1] * self.pw[r-l+1] + self.mod) % self.mod


def solve(cas):
    n, = inp()
    t = input()
    rt = t[::-1]

    debug(t, rt)
    h = Hash(t, 214131331, 9898798161)
    rh = Hash(rt, 214131331, 9898798161)

    if h.get(0, n-1) == rh.get(0, n-1):
        print(t[n:])
        print(0)
        return
    for i in range(n):
        if h.get(0, i) == rh.get(n-i-1, n-1) and h.get(i+1, n-1) == rh.get(0, n-i-2):
            print(t[i+1:i+n+1][::-1])
            print(i+1)
            return
    print(-1)

        

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
