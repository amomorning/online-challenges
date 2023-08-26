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

d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def solve(cas):
    H, W = inp()
    S = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '>':
                for k in range(j+1, W):
                    if S[i][k] == '.':
                        S[i][k] = '-'
                    elif S[i][k] == '|':
                        continue
                    else:
                        break
            elif S[i][j] == '<':
                for k in range(j-1, -1, -1):
                    if S[i][k] == '.':
                        S[i][k] = '-'
                    elif S[i][k] == '|':
                        continue
                    else:
                        break
            elif S[i][j] == '^':
                for k in range(i-1, -1, -1):
                    if S[k][j] == '.':
                        S[k][j] = '|'
                    elif S[k][j] == '-':
                        continue
                    else:
                        break
            elif S[i][j] == 'v':
                for k in range(i+1, H):
                    if S[k][j] == '.':
                        S[k][j] = '|'
                    elif S[k][j] == '-':
                        continue
                    else:
                        break
            elif S[i][j] == 'S':
                start = (i, j)
            elif S[i][j] == 'G':
                end = (i, j)
    
    # for i in range(H):
    #     debug(''.join(S[i]))
    
    q = collections.deque()
    q.append((start, 0))
    while q:
        (x, y), d = q.popleft()
        # debug(x, y, d)
        if (x, y) == end:
            print(d)
            return
        for dx, dy in d4:
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W and (S[nx][ny] == '.' or S[nx][ny] == 'G'):
                q.append(((nx, ny), d+1))
                S[nx][ny] = 'O'
    print(-1)



cas = 1
for _ in range(cas):
    solve(_)

