import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


inp = lambda : list(map(int, input().split()))

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

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def solve(cas):
    n, m = inp()
    pts = [inp() for _ in range(n+m)]
    dp = [[math.inf] * (n+m) for _ in range(2**(n+m+1))]

    ans = math.inf
    for i in range(2**(n+m)):
        speed = 1
        for j in range(n, n+m):
            if (i >> j) & 1:
                speed *= 2
        for j in range(n+m):
            if (i >> j) & 1: continue

            cur = i | (1<<j)

            if i == 0:
                dis = distance(pts[j], [0, 0]) / speed
                dp[cur][j] = min(dp[cur][j], dis)
            else:
                for k in range(n+m):
                    if k == j: continue
                    dis = distance(pts[j], pts[k]) / speed
                    dp[cur][j] = min(dp[cur][j], dp[i][k] + dis)
                    # debug('---------', dp[cur][j], dp[i][k], i, dis)
            
            cnt = 0
            for k in range(n):
                if (cur >> k) & 1:
                    cnt += 1 
            
            if cnt == n:
                tmp = 2 if j >= n else 1
                # debug(j, n, tmp)
                ans = min(ans, dp[cur][j] + distance(pts[j], [0, 0]) / speed / tmp)
                # debug('ans =', ans)

    print(ans)
    

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
