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

def count(d, p, n):
    tot = 0
    h = [0] * (n+1)
    for i in range(n, 1, -1):
        if h[i] == d-1 and p[i-2] != 1:
            tot += 1
        else:
            h[p[i-2]] = max(h[p[i-2]], h[i]+1)

    return tot
            
            


def solve(cas):
    n, k = inp()
    p = inp()
        
    # print(all_leaves)
        
    l, r = 1, 200000
    while l <= r:
        m = (l + r) >> 1
        if count(m, p, n) <= k:
            ans = m
            r = m - 1
        else:
            l = m + 1
    
    print(ans)

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
