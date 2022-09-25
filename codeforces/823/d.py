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

def solve():
    n = int(input())
    s = input()
    t = input()
    mp = {}
    for i in range(n):
        x, y = s[i], t[n-i-1]
        if x > y: x, y = y, x
        if (x, y) in mp:
            mp[(x, y)] += 1
        else:
            mp[(x, y)] = 1
    
    odd = 0
    for v, x in mp.items():
        if x % 2 and v[0] != v[1]:
            print("NO")
            return
        odd += x % 2

    if odd <= 1:
        print("YES")
    else: print("NO")
    

for _ in range(int(input())):
    solve()
