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
    a = [-1] * n
    for i in range(n):
        a[i] = n-1-i
    debug(a)
    ans = []
    for i in range(n-1, -1, -1):
        if p[i] != -1 and a[p[i]] > a[i]:
            a[p[i]] = a[i]
        ans.append(a[i])
    
    debug(ans)
    cnt = 1
    dp = [0] * n
    for i in range(1, n):
        if ans[i] >= tot[-1]:
        if ans[i] >= ans[i-1]:
            cnt += 1
        else:
            break
    print(cnt)



cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
