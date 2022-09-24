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

n, k = inp() 
a = sorted(inp())
a.reverse()

takahashi = 0
aoki = 0
while n > 0:
    i = 0
    while i < k and a[i] > n:
        i += 1
    if i == k: break
    takahashi += a[i]
    n -= a[i]

    i = 0
    while i < k and a[i] > n:
        i += 1
    if i == k: break
    aoki += a[i]
    n -= a[i]

print(takahashi)

    
