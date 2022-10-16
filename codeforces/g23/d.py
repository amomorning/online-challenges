import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


inp = lambda f=int: list(map(f, input().split()))

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


def bfs(G, k, p):
    q = collections.deque([0])
    p[0].add(k)

    topo = []

    while q:
        u = q.popleft()
        topo.append(u)
        m = len(G[u])
        for v in G[u]:
            for s in p[u]:
                p[v].add(math.floor(s/m))
                p[v].add(math.ceil(s/m))
            q.append(v)
    
    topo.reverse()
    return topo

    

def solve(cas):
    n, k = inp()
    p = inp(lambda x: int(x)-1)
    c = inp()
    
    G = [[] for _ in range(n)]
    for i, x in enumerate(p):
        G[x].append(i+1)


    status = [set() for _ in range(n)]
    topo = bfs(G, k, status)

    vis = [0] * n
    dp = [{} for _ in range(n)]
    for u in topo:
        for k in status[u]:
            dp[u][k] = k*c[u]

            m = len(G[u])
            tmp = []
            for v in G[u]:
                tmp.append((dp[v][math.ceil(k/m)] - dp[v][math.floor(k/m)], v))
            tmp = sorted(tmp, reverse=True, key=lambda x:x[0])
            for i in range(m):
                v = tmp[i][1]
                if i < k%m:
                    dp[u][k] += dp[v][math.ceil(k/m)]
                else:
                    dp[u][k] += dp[v][math.floor(k/m)]
    print(dp[0][k])
    # print(status)
    # print(topo)
    
cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
