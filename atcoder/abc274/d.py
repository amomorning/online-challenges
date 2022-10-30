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
    n, x, y = inp()
    a = inp()
    if n % 2 == 0:
        d = [set() for _ in range(n//2)]
        p = [set() for _ in range(n-n//2+1)]
        d[0].add(a[0])
        p[0].add(0)
        for i in range(1, n//2):
            for b in d[i-1]:
                d[i].add(b + a[i*2])
                d[i].add(b - a[i*2])
        for i in range(1, n-n//2+1):
            for b in p[i-1]:
                p[i].add(b + a[i*2-1])
                p[i].add(b - a[i*2-1])
        if x in d[n//2-1] and y in p[n-n//2]:
            print("Yes")
        else:
            print("No")
    else:
        d = [set() for _ in range(n//2+1)]
        p = [set() for _ in range(n-n//2)]
        d[0].add(a[0])
        p[0].add(0)
        for i in range(1, n-n//2):
            for b in p[i-1]:
                p[i].add(b + a[i*2-1])
                p[i].add(b - a[i*2-1])
        for i in range(1, n//2+1):
            for b in d[i-1]:
                d[i].add(b + a[i*2])
                d[i].add(b - a[i*2])
        if x in d[n//2] and y in p[n-n//2-1]:
            print("Yes")
        else:
            print("No")
                

        

        
        
            
            
        

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
