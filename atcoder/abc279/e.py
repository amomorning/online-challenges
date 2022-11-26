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
    n, m = inp()
    a = inp(lambda x: int(x)-1)
    perm = list(range(n))
    for i in range(m-1, -1, -1):
        perm[a[i]], perm[a[i]+1] = perm[a[i]+1], perm[a[i]]
    
    cur = 0
    for i in range(m):
        perm[a[i]], perm[a[i]+1] = perm[a[i]+1], perm[a[i]]
        print(perm[cur]+1)
        if cur == a[i]:
            cur += 1
        elif cur == a[i]+1:
            cur -= 1
    


def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

cas = 1
for _ in range(cas):
    solve(cas)
