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
    n, = inp()
    req = make_arr(3, 3)(collections.deque)
    sid = 'win'

    for k in range(n):
        s = input()
        for i in range(3):
            for j in range(3):
                if s.count(sid[j]) == 0 and s.count(sid[i]) >= 2:
                    req[i][j].append(k)
    
    ans = []
    for i in range(3):
        for j in range(3):
            while req[i][j] and req[j][i]:
                p = req[i][j].popleft()
                q = req[j][i].popleft()
                ans.append((p, i, q, j))

    for i, j, k in itertools.permutations([0, 1, 2]):
        while req[i][j] and req[j][k] and req[k][i]:
            p = req[i][j].popleft()
            q = req[j][k].popleft()
            r = req[k][i].popleft()
            ans.append((p, i, q, j))
            ans.append((q, i, r, k))
        
    print(len(ans))
    for p, i, q, j in ans:
        print(p+1, sid[i], q+1, sid[j])
                

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
