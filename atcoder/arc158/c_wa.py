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
    raw = inp()
    m = len(str(max(raw)))
    mp = make_arr(m, 10, 10)(lambda:0)
    # mp[0] = [0] * 10
    for i in range(n):
        tmp = str(raw[i])
        k = len(tmp)
        tmp = '0'*(m-k) + tmp + '0'
        debug(tmp)
        for j in range(m):
            mp[j][int(tmp[m-1-j])][int(tmp[m-j])] += 1
            
    # debug(mp)
    tot = 0
    debug(mp)
    for i in range(n):
        tmp = str(raw[i])
        k = len(tmp)
        tmp = '0'*(m-k) + tmp
        for j in range(m):
            cur = int(tmp[m-1-j])
            if j:
                last = int(tmp[m-j])
                up = 0
                for p in range(10):
                    up = 0
                    for q in range(10-last, 10):
                        up += mp[j][p][q]
                    
                    debug('up', up, sum(mp[j][p]))
                    tot += (p+cur) % 10 * (sum(mp[j][p]) - up)
                    tot += (p+cur+1) % 10 * up
                    
                    if j == m-1:
                        tot += (p+cur+1) // 10 * up
                        tot += (p+cur) // 10 * (sum(mp[j][p]) - up)
            else:
                for p in range(10):
                    tot += (p + cur) % 10 * sum(mp[j][p])
                    if j == m-1:
                        tot += (p + cur) // 10 * sum(mp[j][p])

            # if j == k-1:
            #     for p in range(10-cur, 10):
            #         tot += sum(mp[j][p])
            debug(tot)
    print(tot)
                    
                
        

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

