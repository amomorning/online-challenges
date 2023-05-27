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

def is_beautiful(s):
    cur = 0
    for i in range(len(s)):
        if s[i] == '(':
            cur += 1
        if s[i] == ')':
            cur -= 1
        if cur < 0:
            return False
    if cur == 0: 
        return True
    return False

def solve(cas):
    n, = inp()
    s = input()
    if n%2 != 0: 
        print(-1)
        return
    if is_beautiful(s) or is_beautiful(s[::-1]):
        print(1)
        printf([1] * len(s))
        return
    
    b = 0
    l, r = [], []
    while b<n and s[b] != '(': 
        r.append((s[b], b))
        b += 1
    if b == n: 
        print(-1)
        return
    cur = 1
    l.append((s[b], b))
    for i in range(b+1, n):
        if s[i] == '(':
            cur += 1
            l.append((s[i], i))
        if s[i] == ')':
            if cur > 0:
                cur -= 1
                l.append((s[i], i))
            else:
                r.append((s[i], i))
    ll = []
    while cur > 0 and l:
        u, v = l.pop()
        if u == '(':
            r.append((u, v))
            cur -= 1
        else:
            ll.append((u, v))
    
    if cur > 0:
        print(-1)
        return
            
    l += ll

    l = sorted(l, key=lambda x: x[1])
    r = sorted(r, key=lambda x: x[1])
    a = ''.join([x[0] for x in l])
    b = ''.join([x[0] for x in r])
    debug(b)

    if is_beautiful(b[::-1]) and is_beautiful(a):
        print(2)
        t = [1] * n
        for u, v in r:
            t[v] = 2
        printf(t)
    else:
        print(-1)
    


    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

