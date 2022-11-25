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
    n, x = inp()
    if n % x != 0: 
        print(-1)
        return
    p = list(range(n+1))
    p[n] = 1 
    p[1] = x
    if x != n: p[x] = n

    while True:
        flag = True
        for t in range(x+x, n, x):
            if n % t == 0:
                p[x], p[t] = p[t], p[x]
                x = t
                flag = False
                break
        if flag:
            printf(p[1:])
            return

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
