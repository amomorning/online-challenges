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

def equals(a, b):
    if a[0] == b[0] and a[1] == b[1]:
        return True
    if a[0] == b[1] and a[1] == b[0]:
        return True
    return False

for _ in range(int(input())):
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
    
    odd, sym = 0, 0
    for x, y in mp.keys():
        if mp[(x, y)] % 2 == 1:
            odd += 1
            if x == y: sym += 1
    debug(odd, sym)
    if odd == sym and n % 2 == sym:
        print("YES")
    else: print("NO")
    
