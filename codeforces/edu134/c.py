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

for _ in range(int(input())):
    n = int(input())
    a = inp()
    b = inp()

    mn = []
    for i in range(n):
        idx = bisect.bisect_left(b, a[i])
        mn.append(b[idx] - a[i])
    
    mx = []
    curmax = b[-1]
    for i in range(n-1, -1, -1):
        idx = bisect.bisect_left(b, a[i])
        mx.append(curmax - a[i])
        # print(idx, i)
        if idx == i:
            curmax = b[idx-1]
            
    mx.reverse()
    printf(mn)
    printf(mx)

