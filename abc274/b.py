import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


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

def solve(cas):
    n, m = inp()
    c = []
    for i in range(n):
        c.append(input())
    for i in range(m):
        tot = 0
        for j in range(n):
            if c[j][i] == '#':
                tot += 1
        print(tot, end=' ')
            

cas = 1
for _ in range(cas):
    solve(cas)
