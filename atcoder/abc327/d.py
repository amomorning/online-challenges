#!/usr/bin/env python3
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


# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout



def solve(cas):
    n, m = inp()
    a = inp(lambda x: int(x)-1)
    b = inp(lambda x: int(x)-1)
    G = [[] for _ in range(n)]
    for i in range(m):
        u, v = a[i], b[i]
        G[u].append(v)
        G[v].append(u)
        if u == v:
            print('No')
            return
    co = [None] * n
    def colorize(s):
        co[s] = True
        q = collections.deque([s])
        while q:
            u = q.popleft()
            for v in G[u]:
                if co[v] is None:
                    co[v] = not co[u]
                    q.append(v)
                elif co[v] == co[u]:
                    return False
        return True

    for i in range(n):
        if co[i] is None:
            status = colorize(i)
            if not status:
                print('No')
                return
    print('Yes')


cas = 1
for _ in range(cas):
    solve(_)

