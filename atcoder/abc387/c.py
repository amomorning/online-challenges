#!/usr/bin/env python3
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


# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def calc_brute(n):
    res = []
    for i in range(10, n+1):
        s = str(i)
        flag = True
        for j in range(1, len(s)):
            if int(s[j]) >= int(s[0]):
                flag = False
        if flag:
            res.append(i)
    return len(res)

def solve(cas):
    l, r = inp()

    def calc(n):
        s = str(n)
        tot = 0
        for i in range(1, len(s)-1):
            for j in range(1, 10):
                tot += j**i
        
        for i in range(1, int(s[0])):
            tot += i**(len(s)-1)
        
        first = int(s[0])
        for i in range(1, len(s)):
            tot += min(first, int(s[i])) * first**(len(s)-1-i)
            if s[i] >= s[0]:
                break

        flag = True
        for i in range(1, len(s)):
            if int(s[i]) >= int(s[0]):
                flag = False
        if flag:
            tot += 1
        return tot
    
    ans = calc(r) - calc(l)
    flag = True
    sl = str(l)
    for i in range(1, len(sl)):
        if int(sl[i]) >= int(sl[0]):
            flag = False
    if flag:
        ans += 1
    print(ans)


cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

