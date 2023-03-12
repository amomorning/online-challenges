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
    a = inp()
    ans = 0
    m = 0
    for i in range(n):
        ans += sum(map(int, list(str(a[i]))))
        m = max(m, len(str(a[i])))
    ans = ans * 2 * n
    
    for k in range(m):
        x = [a[i]%10**(k+1) for i in range(n)]
        x = sorted(x)
        for i in range(n):
            p = bisect.bisect_left(x, 10**(k+1) - x[i])
            ans -= 9 * (len(x) - p)
    print(ans)
    

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

