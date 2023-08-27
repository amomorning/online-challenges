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
        while p >= 0: tot += self.bits[p]; p -= ~p & p + 1
        return tot
    
    def add(self, p, x):
        while p < self.n: self.bits[p] += x; p += ~p & p + 1


def solve(cas):
    n, = inp()
    s = [list(map(int, list(input()))) for _ in range(n)]

    flip = 0
    arr = []

    cnt = 0

    for i in range(n):
        tmp = [0] * n
        c0 = Fenwick(n)
        c1 = Fenwick(n)

        new_arr = []
        for x, y in arr:
            l, r = y-(i-x), y+(i-x)
            if l < 0: l = 0
            if r >= n: r = n-1
            # debug(l, r)
            if l == 0 and r == n-1: 
                flip ^= 1
                continue
            c0.add(l, -(l-1))
            c1.add(l, 1)
            c0.add(r+1, r)
            c1.add(r+1, -1)
            new_arr.append((x, y))

        for j in range(n):
            tmp = c0.ask(j) + c1.ask(j)*j - c0.ask(j-1) - c1.ask(j-1)*(j-1)
            if (s[i][j] + tmp + flip) % 2 == 0: continue
            cnt += 1
            new_arr.append((i, j))

        arr = new_arr
    print(cnt)
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

