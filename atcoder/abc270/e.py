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

n, k = inp() 
a = list(zip(inp(), range(n)))
a = sorted(a)

b = [0]*n
cur = 0
tot = 0
for i in range(n):
    tmp = tot + (a[i][0] - cur) * (n-i)

    if tmp < k:
        tot += (a[i][0] - cur) * (n-i)
        cur = a[i][0]
        b[a[i][1]] = 0
        continue
    else:
        num = (k-tot)//(n-i)
        tot += num * (n-i)
        for j in range(i, n):
            b[a[j][1]] = a[j][0] - cur - num
        break

for i in range(n):
    if b[i] > 0 and tot < k:
        b[i] -= 1
        tot += 1

printf(b)

