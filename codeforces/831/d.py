import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


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
    n, m, k = inp()
    a = inp(lambda x: int(x)-1)
    cur = k - 1
    rest = n * m - 2
    on_rest = [0] * k
    for x in a:
        if x == cur:
            if rest < 2:
                print("TIDAK")
                return
            cur -= 1
            while on_rest[cur] == 1:
                on_rest[cur] = 0
                cur -= 1
                rest += 1
            continue
        on_rest[x] = 1
        rest -= 1
        if rest < 1:
            print("TIDAK")
            return
    print("YA")
        

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
