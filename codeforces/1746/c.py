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

    subs = []
    for i in range(1, n):
        if a[i] < a[i-1]:
            subs.append((a[i-1]-a[i], i))
    
    ans = [1] * n
    subs = sorted(subs, key=lambda x: x[0])
    cur = 0 
    for d, i in subs:
        while cur+1 < d:
            cur += 1
        while cur < n-1 and ans[cur] != 1:
            cur += 1
        debug(cur, d, i)
        if ans[cur] == 1:
            ans[cur] = i+1
    printf(ans)


cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
