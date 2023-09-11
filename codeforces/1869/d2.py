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
    a = inp()
    avg = sum(a)//n

    if avg*n != sum(a):
        print('NO')
        return
    
    inn = []
    out = []

    for i in range(n):
        if a[i] < avg:
            flag = False
            for j in range(30):
                for k in range(j):
                    if (1<<j) - (1<<k) == avg-a[i]:
                        flag = True
                        inn.append(j)
                        out.append(k)
            if not flag:
                print('NO')
                return
        elif a[i] > avg:
            flag = False
            for j in range(30):
                for k in range(j):
                    if (1<<j) - (1<<k) == a[i]-avg:
                        flag = True
                        out.append(j)
                        inn.append(k)
            if not flag:
                print('NO')
                return
            
    # debug(inn)
    # debug(out)
    cnt = [0]*40                    
    rest = []
    for i in range(len(inn)):
        if abs(inn[i] - out[i]) >= 2:
            cnt[inn[i]] += 1
            cnt[out[i]] -= 1
        else:
            rest.append((inn[i], out[i]))
            
        
    rest = sorted(rest)
    void = 0
    # debug(cnt)
    # debug(rest)
    for i, o in rest:
        # debug(i, o, cnt[i], cnt[o])
        if i > o:
            if cnt[o] < 0:
                cnt[o] += 1
                void -= 1
            else:
                cnt[i] += 1
                cnt[o] -= 1
        else:
            if cnt[i] > 0:
                cnt[i] -= 1
                void += 1
            else:
                cnt[i] += 1
                cnt[o] -= 1

    if void == 0 and cnt.count(0) == len(cnt):
        print("YES")
    else:
        print("NO")
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

