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

def solve(cas):
    n, = inp()
    tiles = []
    for i in range(n):
        a, b = inp()
        if a < b: a, b = b, a
        tiles.append((a, b))

    tiles = sorted(tiles, key=lambda x:x[0])
    ans = 0
    last_a = math.inf
    for a, b in tiles:
        if ans > 0:
            ans -= min(last_a, a) * 2
        ans += (a + b) * 2
        last_a = a
    print(ans)
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
