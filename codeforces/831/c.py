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
    a = inp()
    a = sorted(a)
    ans = -math.inf
    for i in range(2, n):
        tmp = a[i] * 2 - a[0] - a[i-1]
        ans = max(ans, tmp)
    
    for i in range(0, n-2):
        tmp = a[i+1] + a[-1] - a[i] * 2
        ans = max(ans, tmp)
    print(ans)
    
        

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
