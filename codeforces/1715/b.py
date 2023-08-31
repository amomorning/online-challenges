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
    n, k, b, s = inp()
    if b*k <= s <= (n-1)*(k-1) + b*k + (k-1):
        a = [0] * n
        a[0] = b*k
        res = s - b*k
        for i in range(n):
            if res >= (k-1):
                a[i] += k-1
                res -= (k-1)
            else:
                a[i] += res
                res -= res

        print(' '.join(map(str, a))) 
    else:
        print(-1)

