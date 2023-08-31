import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


inp = lambda f=int: list(map(f, input().split()))

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
    p = [-1] + inp(lambda x: int(x)-1)
    a, dp = [1] * n, [0] * n
    for i in range(n-1, -1, -1):
        dp[i] = max(dp[i], a[i])
        if i:
            dp[p[i]] += dp[i]
            a[p[i]] = max(a[p[i]], a[i]+1)
    
    print(dp[0])



cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
