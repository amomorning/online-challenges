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
    n, = inp()
    a = [[], [], []]
    for i in range(n):
        u, l, d, r = inp(lambda x: int(x)-1)
        if d-u == 1:
            a[2].append((l, r, i))
        else:
            a[u].append((l, r, i))
    
    for i in range(3):
        a[i] = sorted(a[i])
    
    zeros = []
    b = [[], [], []]
    for i in range(3):
        cur = -1
        for l, r, idx in a[i]:
            if l > cur:
                cur = r
                b[i].append((l, r, idx))
            elif r > cur:
                b[i].append((cur+1, r, idx))
                cur = r
            else:
                zeros.append(idx)
    
    # debug(b)
    result = [[], [], []]
    tmp = [[], []]
    for j, (l, r, idx) in enumerate(b[2]):
        flag = True    
        for i in range(2):
            if len(b[i]) == 0: continue
            bl = bisect.bisect_left(b[i], (l, math.inf, math.inf)) - 1
            ll, rr, _ = b[i][bl]
            # debug(ll, rr, l, r)
            if bl >= 0 and l >= ll and r <= rr:
                tmp[1-i].append((l, r, idx))
                flag = False
                break
        if flag: 
            result[2].append((l, r, idx))
    # debug(result) 
    for i in range(2):
        for l, r, idx in tmp[i]:
            b[i].append((l, r, idx))
        b[i] = sorted(b[i])
    
    c = [[], []]
    for i in range(2):
        cur = -1
        for l, r, idx in b[i]:
            if l > cur:
                cur = r
                c[i].append((l, r, idx))
            elif r > cur:
                c[i].append((cur+1, r, idx))
                cur = r
            else:
                zeros.append(idx)

    # debug(result[2])
    for i in range(2):
        for l, r, idx in c[i]:
            if len(result[2]) == 0:
                result[i].append((l, r, idx))
                continue

            bl = bisect.bisect_left(result[2], (l, math.inf, math.inf))-1
            if bl < 0:
                nr = min(r, result[2][0][0]-1)
                nl = l
            else:
                nl = max(l, result[2][bl][1]+1)
                nr = r
                if bl + 1 < len(result[2]):
                    nr = min(nr, result[2][bl+1][0]-1)
            if nr >= nl and nl >= 0:
                result[i].append((nl, nr, idx))
                debug(nl, nr)
            else:
                zeros.append(idx)

    # debug(result)
    tot = 0
    ans = [None] * n
    w = [1, 1, 2]
    h = [(1, 1), (2, 2), (1, 2)]
    for i in range(3):
        for l, r, idx in result[i]:
            tot += w[i] * (r-l+1)
            ans[idx] = [h[i][0], l+1, h[i][1], r+1]
        
    for idx in zeros:
        ans[idx] = [0, 0, 0, 0]

    print(tot)
    for x in ans:
        printf(x)
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
