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
def cut(a):
    aabb = [math.inf, math.inf, -math.inf, -math.inf]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == '#':
                aabb[0] = min(aabb[0], i)
                aabb[1] = min(aabb[1], j)
                aabb[2] = max(aabb[2], i)
                aabb[3] = max(aabb[3], j)
    return [a[i][aabb[1]:aabb[3]+1] for i in range(aabb[0], aabb[2]+1)]

def match(a, b):
    a = cut(a)
    if len(a) != len(b) or len(a[0]) != len(b[0]): return False
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]: return False
    return True

def check(a, b, x):
    L, R = 20, 20
    h, w = 50, 50
    for i in range(h):
        for j in range(w):
            c = [list('.'*w) for _ in range(h)]
            for k in range(len(a)):
                for l in range(len(a[0])):
                    c[k+L][l+R] = a[k][l]
            if i+len(b)-1 >= h or j+len(b[0])-1 >= w: continue
            for k in range(len(b)):
                for l in range(len(b[0])):
                    if b[k][l] == '#':
                        c[i+k][j+l] = b[k][l]
            if match(c, x):
                return True
    return False

def solve(cas):
    h, w = inp()
    a = [input() for _ in range(h)]
    a = cut(a)
    h, w = inp()
    b = [input() for _ in range(h)]
    b = cut(b)
    h, w = inp()
    x = [input() for _ in range(h)]
    x = cut(x)

    if check(a, b, x) or check(b, a, x):
        print('Yes')
    else:
        print('No')
            

cas = 1
for _ in range(cas):
    solve(_)

