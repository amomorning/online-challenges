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
    n = int(input())
    a = inp()

    ops = []
    b = []
    for i in range(n):
        if a[i] % 2 == a[0] % 2:
            b.append([a[i], i])

    for i in range(len(b)-1, 0, -1):
        if b[i][0] < b[i-1][0]:
            b[i-1][0] = b[i][0]
            a[b[i-1][1]] = b[i][0]
            ops.append((b[i-1][1], b[i][1]))
    
    cur = 0
    for i in range(n):
        if a[i] % 2 != a[0] % 2:
            ops.append((cur, i))
            a[i] = a[cur]
        else:
            cur = i


    print(len(ops))
    for o in ops:
        print(o[0]+1, o[1]+1)
