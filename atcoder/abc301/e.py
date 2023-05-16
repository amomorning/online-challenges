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

def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f

# avaliable on Google, AtCoder
# sys.setrecursionlimit(10**6)
# import numpy as np
# import scipy

d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def solve(cas):
    H, W, T = inp()
    A = [list(input()) for _ in range(H)]

    candy = []
    for i in range(H):
        for j in range(W):
            if A[i][j] == 'o':
                candy.append((i, j))
            if A[i][j] == 'S':
                s = (i, j)
            if A[i][j] == 'G':
                t = (i, j)
    N = len(candy)
    dis = make_arr(N+2, N+2)(lambda:-1)
    
    def bfs(x, y, i):
        d = make_arr(H, W)(lambda: math.inf)
        q = collections.deque()
        q.append((x, y))
        d[x][y] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in d4:
                xx, yy = x+dx, y+dy
                if xx >= 0 and yy >= 0 and xx < H and yy < W:
                    if A[xx][yy] != '#' and d[xx][yy] > d[x][y] + 1:
                        q.append((xx, yy))
                        d[xx][yy] = d[x][y] + 1
                        
        for j, (xx, yy) in enumerate(candy+[s, t]):
            dis[i][j] = d[xx][yy]
            dis[j][i] = d[xx][yy]
        
    for i, (x, y) in enumerate(candy+[s, t]):
        bfs(x, y, i)
    # debug(dis)
    # dp[0010001][i] 2^18 cur_pos = min_steps
    if dis[N][N+1] > T:
        print(-1)
        return
    dp = make_arr(2**N, N)(lambda: T+1)
    for j in range(N):
        dp[1 << j][j] = dis[N][j]
    
    for i in range(1, 2**N):
        w = i
        while w > 0:
            z = w & -w
            j = popcount(z - 1)
            w -= z

            if dp[i][j] >= T:
                continue

            t = (2 ** N - 1) ^ i
            while t > 0:
                y = t & -t
                k = popcount(y - 1)
                t -= y

                g = i ^ y
                dp[g][k] = min(dp[g][k], dp[i][j] + dis[j][k])
    
    ans = 0
    for i in range(2**N):
        for j in range(N):
            if dp[i][j] <= T and dp[i][j] + dis[j][N+1] <= T:
                ans = max(ans, bin(i)[2:].count('1'))
                break
            
    print(ans)

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(_)

