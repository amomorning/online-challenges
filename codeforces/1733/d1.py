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
    n, x, y = inp()
    a = list(map(int, list(input())))
    b = list(map(int, list(input())))
    ids = []
    for i in range(n):
        if a[i] != b[i]:
            ids.append(i)

    if len(ids) % 2:
        print(-1)
        continue
    
    if len(ids) == 2:
        if ids[0]+1 == ids[1]:
            print(min(x, 2*y))
        else:
            print(y)
    else:
        print(len(ids)//2*y)
    
    
