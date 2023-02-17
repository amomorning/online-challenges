#!/usr/bin/env python3
import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')

# LOCAL = False

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

def count(h, n):
    ret = [0] * n
    q = collections.deque()
    for i in range(0, n):
        if i:
            ret[i] = ret[i-1]
        debug('before:', q)
        if q:
            l, r, hr = q.popleft()
        else:
            q.append((i, i, h[i]))
            continue

        assert r == i-1
        if h[i] == hr+1:
            r += 1
            q.appendleft((l, r, h[i]))
        elif h[i] > hr:
            q.appendleft((l, r, hr))
            q.appendleft((i, i, h[i]))
        else:
            cur = h[i]
            while q and cur <= hr and cur+l-r >= 0:
                ret[i] += (r-l+1) * (hr-cur+1)
                cur = cur-1+l-r
                l, r, hr = q.popleft()
                debug(f'{cur=}', f'{ret[i]=}')
                debug(l, r, hr)
            
            if cur-1 > hr:
                q.appendleft((l, r, hr))
                q.appendleft((r+1, i, h[i]))
            elif cur + l - r < 1:
                    
                debug(l, r, hr, cur)
                p = r-cur+1
                # debug(r, p, hr, cur)
                ret[i] += (r-p) * (hr-cur+1)
                ret[i] += (hr+l-r + hr+p-r) * (p-l+1) // 2
                while q:
                    l, r, hr = q.popleft()
                    ret[i] += (hr+l-r + hr) * (r-l+1) // 2
                debug(f'{ret[i]=}', (r-p) * (hr-cur+1), (hr+l-r + hr+p-r) * (p-l) // 2)
                q.appendleft((p, i, h[i]))
            else:
                ret[i] += (r-l+1) * (hr-cur+1)
                q.appendleft((l, i, h[i]))
        debug('after:', q)
        debug('-----------------')
            
            
    return ret
                


def solve(cas):
    n, = inp()
    h = inp()
    l = count(h, n)
    r = count(h[::-1], n)[::-1]
    ans = sum(h)
    debug(l)
    debug(r)
    for i in range(n):
        ans = min(ans, l[i] + r[i] + h[i])
    print(ans)
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

