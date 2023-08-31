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
    n, m, sx, sy, d = map(int, input().split()); sx -= 1; sy -= 1

    if sx - d <= 0 and sx + d >= n-1:
        print(-1)
    elif sy - d <= 0 and sy + d >= m-1:
        print(-1)
    elif sx + d >= n-1 and sy + d >= m-1:
        print(-1)
    elif sx - d <= 0 and sy - d <= 0:
        print(-1)
    else:
        print(n+m-2)
        
        
        
