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


# quick power
MOD = 998244353
def qpow(a, b):
    ans = 1
    while b:
        if b & 1: ans = ans * a % MOD
        a = a * a % MOD; b >>= 1
    return ans

def solve(cas):
    s = 1
    q = collections.deque([s])
    l = 0
    for _ in range(int(input())):
        a = inp()
        if a[0] == 1:
            q.append(a[1])
            s = (s*10+a[1]) % MOD
            l += 1
        if a[0] == 2:
            u = q.popleft()
            s = (s - u * qpow(10, l) % MOD + MOD) % MOD
            l -= 1
        if a[0] == 3:
            print(s)
            

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

