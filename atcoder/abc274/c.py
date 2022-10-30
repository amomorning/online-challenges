import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


inp = lambda f=int: list(map(f, input().split()))

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
    n, = inp()    
    a = inp(lambda x: int(x)-1)
    d = [-1] * (2*n+1)
    d[0] = 0
    for i in range(n):
        d[2*i+1] = d[a[i]] + 1
        d[2*i+2] = d[a[i]] + 1
    for x in d:
        print(x)
        



cas = 1
for _ in range(cas):
    solve(cas)
