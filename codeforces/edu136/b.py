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
    n = int(input())
    d = inp()
    a = [d[0]]
    for i in range(1, n):
        if d[i] == 0:
            a.append(a[i-1])
        elif d[i] > a[i-1]:
            a.append(a[i-1] + d[i])
        else:
            print(-1)
            return 
    printf(a)
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
