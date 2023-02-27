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

def solve(cas):
    n, = inp()
    a = list(map(int, list(input())))
    b = list(map(int, list(input())))
    if sum(a) == 0 and sum(b) == 0:
        print(0)
        return
    if sum(a) == 0 or sum(b) == 0:
        print(-1)
        return
    for i in range(n):
        if b[i] == 1:
            p = i
            break
    ans = []
    if a[p] != 1:
        for i in range(n):
            if a[i] == 1:
                q = i
                break
        na = [0] * n
        for i in range(n-1, -1, -1):
            if i+q-p >= 0 and i+q-p < n:
                na[i] = a[i+q-p]
            else:
                na[i] = 0
        
        for i in range(n):
            a[i] = (a[i] + na[i]) % 2
        ans.append(q-p)
    
    # debug(a)
    # debug(ans)
    for i in range(n):
        if a[i] == 1:
            high = i
    # debug(low, high, p)
    for i in range(p-1, -1, -1):
        if a[i] != b[i]:
            ans.append(high-i)
            na = []
            for j in range(i+1):
                na.append((a[j] + a[j+high-i])%2)
            for j in range(i+1):
                a[j] = na[j]

    for i in range(n):
        if a[i] == 1:
            low = i
            break
    for i in range(p+1, n):
        if a[i] != b[i]:
            ans.append(low-i)
            na = []
            for j in range(i, n):
                na.append((a[j] + a[j+low-i]) % 2)
            for j in range(i, n):
                a[j] = na[j-i]
    
    print(len(ans))
    if len(ans) > 0:
        printf(ans)




cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

