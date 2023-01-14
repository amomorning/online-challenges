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

def calc_boundary(a, B):
    ap = a[0]
    l, r = [a[0], -1], [B+a[0], -1]
    # by, by = b[0], -1
    for i in range(1, len(a)):
        if a[i] <= ap:
            ap = ap - a[i]
            l = [a[i] - l[0], -1 * l[1]]
            r = [B + a[i] - l[0], -1 * l[1]]
        else:
            ap = B + ap - a[i]
            l = [a[i] - l[0], -1 * l[1]]
            r = [a[i] - r[0], -1 * r[1]]
    
    return ap, l, r

def solve(cas):
    n, m = inp()
    s = [input() for _ in range(n)]
    q, = inp()
    a, b = [], []
    for _ in range(q):
        u, v = inp(lambda x: int(x)-1)
        a.append(u)
        b.append(v)
    # ap, bp = a[0], b[0]
    ic, il ,ir = calc_boundary(a, n)
    jc, jl, jr = calc_boundary(b, m)

    debug(ic, il, ir)
    debug(jc, jl, jr)

    t = make_arr(n, m)('#')
    for i in range(n):
        for j in range(m):
            if i <= ic:
                new_i = il[0] + il[1] * i
            else:
                new_i = ir[0] + ir[1] * i
            if j <= jc:
                new_j = jl[0] + jl[1] * j
            else:
                new_j = jr[0] + jr[1] * j
            t[new_i][new_j] = s[i][j]

    for i in range(n):
        print(''.join(t[i]))


cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)

