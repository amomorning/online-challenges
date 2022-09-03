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

    
n, m = map(int, input().split())
a = list(map(int, input().split()))
sa = list(itertools.accumulate(a))
b = [(i+1)*a[i] for i in range(n)]
sb = list(itertools.accumulate(b))

# print(sb, sa)

mx = sb[m-1]
for i in range(m, n):
    mx = max(mx, sb[i] - sb[i-m] - (i-m+1) * (sa[i] - sa[i-m]))
    
print(mx)
