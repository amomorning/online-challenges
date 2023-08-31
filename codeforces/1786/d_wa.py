import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
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


def match_once(mp, ans):
    while mp[1, 0, 2] and mp[1, 2, 0]:
        p = mp[1, 0, 2].popleft()
        q = mp[1, 2, 0].popleft()
        ans.append((q+1, 'i', p+1, 'n'))
    
    while mp[0, 1, 2] and mp[2, 1, 0]:
        p = mp[2, 1, 0].popleft()
        q = mp[0, 1, 2].popleft()
        ans.append((p+1, 'w', q+1, 'n'))
    
    while mp[0, 2, 1] and mp[2, 0, 1]:
        p = mp[2, 0, 1].popleft() 
        q = mp[0, 2, 1].popleft()
        ans.append((p+1, 'w', q+1, 'i'))

def match_twice(mp, ans):
    while mp[2, 0, 1] and mp[1, 2, 0] and mp[0, 1, 2]:
        p = mp[2, 0, 1].popleft()
        q = mp[1, 2, 0].popleft()
        r = mp[0, 1, 2].popleft()
        ans.append((p+1, 'w', q+1, 'i'))
        ans.append((q+1, 'w', r+1, 'n'))
    
    while mp[0, 2, 1] and mp[1, 0, 2] and mp[2, 1, 0]:
        p = mp[0, 2, 1].popleft()
        q = mp[1, 0, 2].popleft()
        r = mp[2, 1, 0].popleft()
        ans.append((p+1, 'i', q+1, 'w'))
        ans.append((q+1, 'n', r+1, 'w'))
    
    while mp[3, 0, 0] and mp[0, 1, 2] and mp[0, 2, 1]:
        p = mp[3, 0, 0].popleft()
        q = mp[0, 1, 2].popleft()
        r = mp[0, 2, 1].popleft()
        ans.append((p+1, 'w', q+1, 'n'))
        ans.append((p+1, 'w', r+1, 'i'))
    
    while mp[0, 3, 0] and mp[1, 0, 2] and mp[2, 0, 1]:
        p = mp[0, 3, 0].popleft()
        q = mp[1, 0, 2].popleft()
        r = mp[2, 0, 1].popleft()
        ans.append((p+1, 'i', q+1, 'n'))
        ans.append((p+1, 'i', r+1, 'w'))
    
    while mp[0, 0, 3] and mp[1, 2, 0] and mp[2, 1, 0]:
        p = mp[0, 0, 3].popleft()
        q = mp[1, 2, 0].popleft()
        r = mp[2, 1, 0].popleft()
        ans.append((p+1, 'n', q+1, 'i'))
        ans.append((p+1, 'n', r+1, 'w'))

def match_thrice(mp, ans):
    while mp[0, 0, 3] and mp[0, 3, 0] and mp[3, 0, 0]:
        p = mp[0, 0, 3].popleft()
        q = mp[0, 3, 0].popleft()
        r = mp[3, 0, 0].popleft()
        ans.append((p+1, 'n', q+1, 'i'))
        ans.append((q+1, 'i', r+1, 'w'))
        ans.append((r+1, 'w', p+1, 'n'))

    
def solve(cas):
    n, = inp()
    mp = dict()
    for i in range(0, 4):
        for j in range(0, 4):
            if i+j > 3: continue
            k = 3-i-j
            mp[i, j, k] = collections.deque()

    all_s = []
    for k in range(n):
        s = input()
        all_s.append(s)

        w = s.count('w')
        i = s.count('i')
        n = s.count('n')
        if w==1 and i==1 and n==1:
            continue
        mp[w, i, n].append(k)
    

    ans = []
    match_thrice(mp, ans)
    match_twice(mp, ans)
    match_once(mp, ans)
    print(len(ans))
    for item in ans:
        printf(item)
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
