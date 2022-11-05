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
    a = inp()
    x, p, q = [], [], []
    for i in range(n):
        cnt = 0
        while a[i] % 2 == 0:
            cnt += 1
            a[i] //= 2
        p.append(cnt)
        cnt = 0
        while a[i] % 3 == 0:
            cnt += 1
            a[i] //= 3
        q.append(cnt)
        x.append(a[i])
    for i in range(n):
        if x[i] != x[0]:
            print(-1)
            return
    mnp, mnq = min(p), min(q)
    ans = 0
    for i in range(n):
        ans += p[i] - mnp
        ans += q[i] - mnq
    print(ans)

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

cas = 1
for _ in range(cas):
    solve(cas)
