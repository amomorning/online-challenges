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

def calc(s):
    x = math.floor(math.sqrt(s))

    while x*x > s: x -= 1

    rest = s - x*x + 1


    if rest <= x:
        return 3*(x-1) + 1
    elif rest <= 2*x:
        return 3*(x-1) + 2
    else:
        return 3*(x-1) + 3

def solve(cas):
    l, r = inp()
    print(calc(r) - calc(l-1))

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)

