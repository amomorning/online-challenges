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
    n, = inp()
    a = sorted(inp())

    if a[0] == a[n-1]:
        print(n*(n-1))
        return


    l, r = 1, 1
    for i in range(1, n):
        if a[i] == a[0]: l += 1
        else: break
    for i in range(n-2, -1, -1):
        if a[i] == a[n-1]: r += 1
        else: break
    print(l*r*2)


cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)

