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

n, m, k = inp() 
a = inp()


ans = 0
for j in range(31, -1, -1):
    cur = 1 << j 
    cost = []
    rest = []
    for i, x in enumerate(a):
        if x & cur:
            rest.append(x - cur)
            cost.append(0)
        else:
            cost.append(cur - ((cur-1)&x))
            
    cost = sorted(cost)

    tot = 0
    if len(cost) >= k:
        for i in range(k):
            tot += cost[i]
    else:
        for i in range(len(cost)):
            tot += cost[i]
        tot += (k - len(cost)) * cur

    if tot <= m:
        m -= tot
        ans += cur
        a = rest

print(ans)
