import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x() for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

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

# avaliable on Google, AtCoder
# sys.setrecursionlimit(10**6)
# import numpy as np
# import scipy

# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def solve(cas):
    a, b = input().split()
    l = []
    n = max(len(a), len(b))
    a = '0'*(n-len(a)) + a
    b = '0'*(n-len(b)) + b

    flag = False
    for i in range(n):
        if flag:
            l.append('9')
            continue
        if a[i] == b[i]:
            l.append(a[i])
        elif a[i] < b[i]:
            flag = True
            l.append(a[i])
    debug(''.join(l))
    r = []
    flag = False
    for i in range(n):
        if flag:
            r.append('0')
            continue
        if l[i] < b[i]:
            r.append(b[i])
            flag = True
        else:
            r.append(l[i])
    debug(''.join(r))
    ans = 0
    for i in range(n):
        ans += abs(ord(r[i]) - ord(l[i]))
    print(ans)


    


cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

