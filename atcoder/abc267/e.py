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


def check(cur_sum, d):
    cur = copy.copy(cur_sum)
    q = collections.deque()
    for u in range(n):
        if cur[u] <= d:
            q.append(u)
            cur[u] = 0

    while q:
        u = q.popleft() 
        for v in G[u]:
            cur[v] -= a[u]
            if cur[v] > 0 and cur[v] <= d:
                q.append(v)
                cur[v] = 0
    for i in range(n):
        if cur[i] > 0: return False
    return True
        


n, m = inp()
a = inp()
G = [[] for _ in range(n)]
for i in range(m):
    u, v = inp()
    u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)
cur_sum = [0] * n
for u in range(n):
    for v in G[u]:
        cur_sum[u] += a[v]
        
l, r = 0, int(1e15)

while l <= r:
    m = (l+r) >> 1
    if check(cur_sum, m):
        r = m - 1 
        ans = m
    else:
        l = m + 1

print(ans)
