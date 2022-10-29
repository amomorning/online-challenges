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

def is_prime(x):
    m = int((x**0.5)) + 1
    for i in range(2, m):
        if x % i == 0:
            return False
    return True

def solve(cas):
    n = int(input())
    for m in range(2, int(1e5)):
        if not is_prime(n + m):
            print(m)
            return
            


cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
