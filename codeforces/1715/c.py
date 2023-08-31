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

    
n, q = inp()
a = inp()
tot = 0
for i in range(n):
    tot += (n-i)*(i+1)

for i in range(1, n):
    if a[i] == a[i-1]:
        tot -= i * (n-i)


for _ in range(q):
    i, x = map(int, input().split()); i -= 1
    if a[i] == x:
        print(tot)
        continue
    if i > 0 and x == a[i-1]:
        tot -= i*(n-i)

    if i < n-1 and x == a[i+1]:
        tot -= (i+1)*(n-i-1)
    
    if i > 0 and a[i] == a[i-1]:
        tot += i*(n-i)
    
    if i < n-1 and a[i] == a[i+1]:
        tot += (i+1)*(n-i-1)

    
    a[i] = x
    print(tot)

        
