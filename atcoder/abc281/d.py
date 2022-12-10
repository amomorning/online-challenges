import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))
sys.setrecursionlimit(10**6)

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


def solve(cas):
    N, K, D = inp()
    a = inp()
    
    F = make_arr(K+1, D)(-1)
    F[0][0] = 0
    for i in range(N):
        G = make_arr(K+1, D)(-1)
        for j in range(K+1):
            for k in range(D):
                G[j][k] = F[j][k]
        for j in range(K):
            for k in range(D):
                if F[j][k] == -1:
                    continue
                tmp = (F[j][k] + a[i]) % D
                G[j+1][tmp] = max(G[j+1][tmp], F[j][k] + a[i])
        F = G
    print(F[K][0])
        
    

cas = 1
for _ in range(cas):
    solve(cas)

