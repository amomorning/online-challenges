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

def transpose(a, n, m):
    b = []
    for j in range(m):
        s = []
        for i in range(n):
            s.append(a[i][j])
        b.append(''.join(s))
    return b

def solve(cas):
    n, m = inp()
    s = sorted(transpose([input() for _ in range(n)], n, m))
    t = sorted(transpose([input() for _ in range(n)], n, m))

    for i in range(m):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")
    

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

cas = 1
for _ in range(cas):
    solve(cas)

