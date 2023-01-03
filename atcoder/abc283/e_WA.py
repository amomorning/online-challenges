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

def solve(cas):
    h, w = inp()
    a = [inp() for _ in range(h)]
    p = [set(), set()]
     
    if a[0][0] != a[0][1]:
        p[0].add(0)
        p[1].add(0)
    for i in range(1, w-1):
        if a[0][i] != a[0][i-1] and a[0][i] != a[0][i+1]:
            p[0].add(i)
            p[1].add(i)
    if a[0][w-1] != a[0][w-2]:
        p[0].add(w-1)
        p[1].add(w-1)
    
    # print(p)
    F = [0, 1]
    for i in range(1, h):
        G = [math.inf, math.inf]
        flag = True
        q = [set(), set()]
        for j in range(w):
            if j in p[0] and a[i][j] != a[i-1][j]:
                flag = False
                break
            if j == 0:
                if a[i][j] != a[i-1][j] and a[i][j] != a[i][j+1]:
                    q[0].add(0)
            elif j == w-1:
                if a[i][j] != a[i-1][j] and a[i][j] != a[i][j-1]:
                    q[0].add(w-1)
            elif a[i][j] != a[i-1][j] and a[i][j] != a[i][j-1] and a[i][j] != a[i][j+1]:
                q[0].add(j)
        if flag:
            G[0] = F[0]
            tmp = set()
            for j in range(w):
                if j in p[1] and a[i][j] != 1-a[i-1][j]:
                    flag = False
                    break
                if j == 0:
                    if a[i][j] != 1-a[i-1][j] and a[i][j] != a[i][j+1]:
                        tmp.add(0)
                elif j == w-1:
                    if a[i][j] != 1-a[i-1][j] and a[i][j] != a[i][j-1]:
                        tmp.add(w-1)
                elif a[i][j] != 1-a[i-1][j] and a[i][j] != a[i][j-1] and a[i][j] != a[i][j+1]:
                    tmp.add(j) 
            if flag:
                if F[1] < F[0]:
                    q[0] = tmp
                    G[0] = F[1]
        else:
            flag = True
            q[0] = set()
            for j in range(w):
                if j in p[1] and a[i][j] != 1-a[i-1][j]:
                    flag = False
                    break
                if j == 0:
                    if a[i][j] != 1-a[i-1][j] and a[i][j] != a[i][j+1]:
                        q[0].add(0)
                elif j == w-1:
                    if a[i][j] != 1-a[i-1][j] and a[i][j] != a[i][j-1]:
                        q[0].add(w-1)
                elif a[i][j] != 1-a[i-1][j] and a[i][j] != a[i][j-1] and a[i][j] != a[i][j+1]:
                    q[0].add(j) 
            if flag:
                G[0] = F[1]

        flag = True
        for j in range(w):
            if j in p[0] and a[i][j] != a[i-1][j]:
                flag = False
                break
            if j == 0:
                if 1-a[i][j] != a[i-1][j] and 1-a[i][j] != a[i][j+1]:
                    q[1].add(0)
            elif j == w-1:
                if 1-a[i][j] != a[i-1][j] and a[i][j] != a[i][j-1]:
                    q[1].add(w-1)
            elif 1-a[i][j] != a[i-1][j] and a[i][j] != a[i][j-1] and a[i][j] != a[i][j+1]:
                q[1].add(j)
        if flag:
            G[1] = F[0]+1
            tmp = set()
            for j in range(w):
                if j in p[1] and 1-a[i][j] != 1-a[i-1][j]:
                    flag = False
                    break
                if j == 0:
                    if 1-a[i][j] != 1-a[i-1][j] and a[i][j] != a[i][j+1]:
                        tmp.add(0)
                elif j == w-1:
                    if 1-a[i][j] != 1-a[i-1][j] and a[i][j] != a[i][j-1]:
                        tmp.add(w-1)
                elif 1-a[i][j] != 1-a[i-1][j] and a[i][j] != a[i][j-1] and a[i][j] != a[i][j+1]:
                    tmp.add(j) 
            if flag:
                if F[1] < F[0]:
                    q[1] = tmp
                    G[1] = F[1]+1
        
        else:
            flag = True
            q[1] = set()
            for j in range(w):
                if j in p[1] and 1-a[i][j] != 1-a[i-1][j]:
                    flag = False
                    break
                if j == 0:
                    if 1-a[i][j] != 1-a[i-1][j] and a[i][j] != a[i][j+1]:
                        q[1].add(0)
                elif j == w-1:
                    if 1-a[i][j] != 1-a[i-1][j] and a[i][j] != a[i][j-1]:
                        q[1].add(w-1)
                elif 1-a[i][j] != 1-a[i-1][j] and a[i][j] != a[i][j-1] and a[i][j] != a[i][j+1]:
                    q[1].add(j) 
            if flag:
                G[1] = F[1]+1
        
        F = G
        p = q
    
    ans = math.inf
    for i in range(2):
        if len(p[i]) == 0:
            ans = min(ans, F[i])
    print(ans) if ans != math.inf else print(-1)
            

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)

