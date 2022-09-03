import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
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

n, m = inp()
a = inp()
dp = [[-math.inf] * (m+1) for _ in range(n)]

for i in range(n):
    dp[i][0] = 0

for i in range(n):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + a[i] * j)
        dp[i][j] = max(dp[i][j], dp[i-1][j])
    
ans = -math.inf
for i in range(n):
    ans = max(ans, dp[i][m])
print(ans)
