#!/usr/bin/env python3
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


# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def cover(a, p, r):
    if dist(a, p) <= r:
        return True



def solve(cas):
    p = inp()
    a = inp()
    b = inp()

    l, r = 0, 10000

    def check(r):
        if cover(a, p, m) and cover(a, (0, 0), m):
            return True
        if cover(b, p, m) and cover(b, (0, 0), m):
            return True
        if (cover(a, p, m) or cover(b, p, m)) and (cover(a, (0,0), m) or cover(b, (0,0), m)):
            if dist(a, b) <= 2*m:
                return True
        return False


    for i in range(100):
        m = (l+r)/2
        if check(m):
            r = m
        else:
            l = m
    print(l)



    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)


