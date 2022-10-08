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
    n, m = inp()    
    l = [[] for _ in range(n)]
    for i in range(m):
        k, *a = inp()
        for j in range(k):
            l[a[j]-1].append(i)
    
    for i in range(n):
        for j in range(i+1, n):
            if not set(l[i]) & set(l[j]):
                print("No")
                return
    print("Yes")

cas = 1
for _ in range(cas):
    solve(cas)
