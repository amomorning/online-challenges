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
    s = input()
    t = input()
    sa = [0]*26
    ta = [0]*26
    tmp = set(map(lambda x: ord(x) - ord('a'), list('atcoder')))
    # debug(tmp)
    for c in s:
        if c != '@':
            sa[ord(c) - ord('a')] += 1
    for c in t:
        if c != '@':
            ta[ord(c) - ord('a')] += 1
    tots = len(s) - sum(sa)
    tott = len(s) - sum(ta)
    for i in range(26):
        if sa[i] == ta[i]: continue
        if not i in tmp:
            # debug(i)
            print("No")
            return
        if sa[i] < ta[i]: tots -= ta[i] - sa[i]
        if sa[i] > ta[i]: tott -= sa[i] - ta[i]
    
    debug(tots, tott)

    if tots == tott and tots >= 0:
        print("Yes")
    else: print("No")
        


cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)


