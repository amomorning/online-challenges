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

n, k = inp() 
a = sorted(inp())

dp = [[0, math.inf] for _ in range(n+1)]
dp[0][1] = 0
for i in range(1, n+1):
    for j in a:
        if i - j < 0: continue
        dp[i][0] = max(dp[i-j][1] + j, dp[i][0])
        dp[i][1] = min(dp[i-j][0], dp[i][1])

# for i in range(1, n+1):
#     debug(i, dp[i][0])
print(dp[n][0])

