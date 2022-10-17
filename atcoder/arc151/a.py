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
    s = input()
    t = input()

    cur = 0
    a = ['0'] * n
    tot = 0
    for i in range(n):
        if s[i] != t[i]: tot += 1
    if tot % 2 != 0:
        print(-1)
        return

    l, r = 0, 0
    for i in range(n):
        if s[i] == t[i]: continue
        if l == tot // 2:
            a[i] = t[i]    
        elif r == tot // 2:
            a[i] = s[i]
        else:
            if s[i] == '0':
                l += 1
            else:
                r += 1

    print(''.join(a))
                
                

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
