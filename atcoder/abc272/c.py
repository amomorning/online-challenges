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
    even = []
    odd = []
    a = sorted(a)
    for i in range(n):
        if a[i] % 2 == 0:
            even.append(a[i])
        else:
            odd.append(a[i])
    ans = -1 
    if len(even) >= 2:
        ans = max(ans, even[-1] + even[-2])
    if len(odd) >= 2:
        ans = max(ans, odd[-1] + odd[-2])
    print(ans)


cas = 1
for _ in range(cas):
    solve(cas)
