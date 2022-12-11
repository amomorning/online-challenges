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


def solve(cas):
    n, m = inp()
    
    a = [n-1] * n
    for i in range(m):
        l, r = inp(lambda x: int(x) - 1)
        if l > r: l, r = r, l
        a[l] = min(a[l], r-1)

    r, tot = n-1, 0
    for l in range(n-1, -1, -1):
        r = min(r, a[l])
        tot += r-l+1
    
    print(tot)
        

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)

