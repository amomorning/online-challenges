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

# avaliable on Google, AtCoder
# sys.setrecursionlimit(10**6)
# import numpy as np
# import scipy

# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout


def find_pos(mask):
    for i in range(mask.bit_length()+1):
        if not (mask & (1<<i)):
            return i
    return None
    
def solve(cas):
    N, T, M = inp()
    dp = make_arr(1<<(N+1), T+1)(lambda: 0)
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = inp(lambda x: int(x)-1)
        G[a].append(b)
        G[b].append(a)
    
    def check_valid(u, all_pos):
        for v in all_pos:
            if v in G[u]:
                return False
            for w in all_pos:
                if v == w: continue
                if w in G[v]:
                    return False
        return True
        
    dp[0][0] = 1
    for t in range(1, T+1):
        for mask in range((1<<(N+1))):
            if dp[mask][t-1] == 0: continue
            u = find_pos(mask)
            if u >= N: break
            umask = mask | (1 << u)
            new_mask = umask
            while new_mask <= (1<<N):
                # debug(bin(new_mask), bin(mask))
                all_pos = []
                for v in range(N):
                    if (not (umask & (1<<v))) and (new_mask & (1<<v)):
                        all_pos.append(v)
                
                if check_valid(u, all_pos):
                    dp[new_mask][t] += dp[mask][t-1]
                    # debug(u, all_pos)

                new_mask = (new_mask+1) | umask
    print(dp[int('1'*N, 2)][T])
            
        

cas = 1
for _ in range(cas):
    solve(_)

