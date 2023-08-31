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
def LongestPalindromicPrefix(s, bogus='#'):
    tmp = s + bogus + s[::-1]
    n = len(tmp)
    lps = [0] * n
    for i in range(1, n):
        m = lps[i - 1]
        while (m > 0 and tmp[m] != tmp[i]):
            m = lps[m - 1]
        if (tmp[i] == tmp[m]):
            m += 1
        lps[i] = m
    return tmp[0 : lps[n - 1]]

def solve(cas):
    s = input()
    p, n = 0, len(s)
    while p < n-p-1 and s[p] == s[n-p-1]: p += 1
    subs = s[p:n-p]
    pre = LongestPalindromicPrefix(subs)
    suf = LongestPalindromicPrefix(subs[::-1])
    mid = pre if len(pre) > len(suf) else suf
    print(s[:p] + mid + s[n-p:])

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

