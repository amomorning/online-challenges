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

def solve(cas):
    a, b, c, d = inp()
    if a == 0:
        print(1)
        return

    u, v = a, a
    ans = a
    if b < c: b, c = c, b
    if b <= a:
        u = u + b - c
        v = v - b + c
        
        has = 1 if d > 0 else 0
        print(a + b + c + min(min(u, v) + has, d))
        return
    else:
        b -= a
        u += a
        v -= a
        tot = a*2
        r = min(b // (2*a), c // (2*a))

        tot += 2*a*r*2
        b -= 2*a*r
        c -= 2*a*r
        # debug(a, b, c, d, u, v)

        while True:
            tmp = min(c, u)
            if tmp == 0: break
            u -= tmp
            v += tmp
            tot += tmp
            c -= tmp
            # debug(a, b, c, d, u, v)

            tmp = min(b, v)
            if tmp == 0: break
            u += tmp
            v -= tmp
            tot += tmp
            b -= tmp
            # debug(a, b, c, d, u, v)

        has = 1 if b + c + d > 0 else 0
        tot += min(min(u, v) + has, d)
        print(tot)

            
            
    
    
    
    


cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
