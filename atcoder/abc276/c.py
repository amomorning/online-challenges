
import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
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
    p = inp()

    for i in range(n-1, -1, -1):
        if p[i-1] > p[i]:
            
            mx = p[i]
            mxi = i
            for j in range(i, n):
                if p[j] > mx and p[j] < p[i-1]:
                    mx = p[j]
                    mxi = j
            p[i-1], p[mxi] = p[mxi], p[i-1]

            res = p[:i] + sorted(p[i:], reverse=True)
            printf(res)
            return

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

cas = 1
for _ in range(cas):
    solve(cas)


