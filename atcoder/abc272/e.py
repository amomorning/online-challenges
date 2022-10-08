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

def mex(a):
    a = sorted(a)
    for i in range(len(a)):
        if i != a[i]:
            return i
    return len(a)

def solve(cas):
    n, m = inp()    
    a = inp()
    ans = [0] * m
    mp = [set() for _ in range(m+1)]
    for i in range(n):
        k = 1
        if a[i] < 0:
            k = (-a[i])//(i+1)
        while a[i] + k*(i+1) <= n and k <= m:
            if a[i] + k*(i+1) >= 0:
                mp[k].add(a[i] + k*(i+1))
            k += 1
    for i in range(1, m+1):
        print(mex(mp[i]))

cas = 1
for _ in range(cas):
    solve(cas)
