import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
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

for _ in range(int(input())):
    n, k = inp()
    a = list(zip(inp(), range(n)))
    a = sorted(a, reverse=True)
    vis = [0] * k
    tot = 0
    for i in range(n):
        if vis[a[i][1]%k] == 0:
            tot += a[i][0]
            vis[a[i][1]%k] = 1
    print(tot)
