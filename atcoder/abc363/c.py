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

def check_k_palindrome(s, k):
    for i in range(len(s) - k + 1):
        # debug(s[i:i+k], '>', s[i:i+k][::-1])
        if s[i:i+k] == s[i:i+k][::-1]:
            return True
    return False
        

def solve(cas):
    n, m = inp()
    s = input()

    dic = {}
    for c in s:
        dic[c] = dic.get(c, 0) + 1
    tot = 0
    ans = 1
    for i in range(len(s)):
        ans *= i + 1
    for k, v in dic.items():
        if v >= 2:
            tot += v // 2
        ans //= v
    if tot < m//2:
        print(ans)
        return

    cnt = 0
    mp = {}
    for p in itertools.permutations(range(n), n):
        t = [s[i] for i in p]
        t = ''.join(t)
        if t in mp:
            continue
        mp[t] = 1
        # debug(t)
        if check_k_palindrome(t, m):
            cnt += 1
    # debug(cnt, len(mp))
    debug(ans, len(mp))
    print(len(mp) - cnt)

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

