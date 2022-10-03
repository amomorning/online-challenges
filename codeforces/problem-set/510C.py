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

def ordc(c):
    return ord(c) - ord('a')

def char(c):
    return chr(ord('a') + c)

def toposort(G, topo=[]):
    d = [0] * len(G)
    for vs in G:
        for v in vs:
            d[v] += 1

    q = collections.deque([u for u in range(len(G)) if d[u] == 0])
    while q:
        u = q.popleft()
        topo.append(u)
        for v in G[u]:
            d[v] -= 1
            if d[v] == 0:
                q.append(v)

    if sum(d):
        return False
    return True
            

def solve(cas):
    n, = inp()
    s = []
    for i in range(n):
        s.append(input())
    
    G = [[] for _ in range(26)]
    for a, b in zip(s, s[1:]):
        flag = True
        for x, y in zip(a, b):
            if x != y:
                flag = False
                G[ordc(x)].append(ordc(y))
                break
        if flag and len(a) > len(b):
            return
    topo = []
    if toposort(G, topo):
        print(''.join(map(char, topo)))
    else:
        print('Impossible')

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
