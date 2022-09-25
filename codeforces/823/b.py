import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda : list(map(int, input().split()))

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

eps = 1e-6
def cmp(x):
    if x < -eps: return -1
    if x > eps: return 1
    return 0

def check(m, x, y):
    lm, rm = 0, 0
    for xi, yi in zip(x, y):
        # left
        if cmp(xi-m) <= 0:
            lm = max(lm, m-xi+yi)
        if cmp(xi-m) >= 0:
            rm = max(rm, xi-m+yi)
    return cmp(lm - rm) <= 0
            
        

for _ in range(int(input())):
    n = int(input())

    x = inp()
    y = inp()

    l, r = 0, 1e8
    ans = 0
    while cmp(l-r) <= 0:
        m = (l+r)/2.0
        if check(m, x, y):
            ans = m
            l = m+eps
        else:
            r = m-eps
    print(ans)
        
