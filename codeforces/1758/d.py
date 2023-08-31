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
    if n == 2:
        print(1, 3)
        return
    if n == 4:
        print(2, 3, 5, 6)
        return
    w = (n * n + 3 * n + 2) // 2
    p = w//n
    ans = list(range(p+1, n+p+1))
    
    for i in range(w%n+1):
        ans[n-i-1] += 1
    ans[0] -= 1
    # debug(max(ans), min(ans), sum(ans))
    printf(ans)
        

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
