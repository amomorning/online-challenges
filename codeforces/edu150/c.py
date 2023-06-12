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

def get(c):
    return ord(c) - ord('A') + 1


def solve(cas):
    s = list(map(lambda c: ord(c) - ord('A') , list(input())))
    vis = [0] * 5
    n = len(s)
    if n == 1:
        print(10**4)
        return
    sign = [1] * n
    for i in range(n-1, -1, -1):
        vis[s[i]] = 1
        for j in range(s[i]+1, 5):
            if vis[j] == 1:
                sign[i] = -1
        
    left, leftE = [], []
    for i in range(n):
        if s[i] == 5:
            left.append(0)
            leftE.append(10**s[i])
        else:
            left.append(10**s[i])
            leftE.append(0)
    
    left = list(itertools.accumulate(left))
    leftE = list(itertools.accumulate(leftE))

    right = []
    for i in range(n-1, -1, -1):
        right.append(sign[i] * (10 ** s[i]))
    right = list(itertools.accumulate(right))

    ans = max(right[n-1], 10**4 + right[n-2])
    for i in range(1, n):
        if n-i-2 >= 0:
            ans = max(ans, -left[i-1] + leftE[i-1] + 10**4 + right[n-i-2])
        else:
            ans = max(ans, -left[i-1] + leftE[i-1] + 10**4)
    
    print(ans)
        
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

