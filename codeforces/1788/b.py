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
def sum_digit(x):
    d = map(int, list(str(x)))
    return sum(d)

def solve(n):
    n, = inp()
    l = n//2
    r = n-l
    if abs(sum_digit(r) - sum_digit(l)) > 1:
        tot = sum_digit(n)
        l = 0
        for d in map(int, list(str(n))):
            if sum_digit(l*10 + d) <= tot//2:
                if l: l*=10
                l += d
            else:
                l *= 10
        # debug(l, r)
        tmp = (sum_digit(n-l) - sum_digit(l))//2
        print(l+tmp, n-l-tmp)
            
    else:
        print(l, r)



cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

