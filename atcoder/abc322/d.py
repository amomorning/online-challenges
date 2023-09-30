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

    
def rotate(pattern):
    return [list(reversed(x)) for x in zip(*pattern)]

def copy(pattern):
    return [x[:] for x in pattern]

def printp(pattern):
    for i in range(len(pattern)):
        print(''.join(pattern[i]))

def cut(pattern):
    ll, rr = -1, -1
    l, r = 4, 4
    for i in range(4):
        for j in range(4):
            if pattern[i][j] == '#':
                l = min(l, i)
                r = min(r, j)
                ll = max(ll, i)
                rr = max(rr, j)
    return [x[r:rr+1] for x in pattern[l:ll+1]]

def count(pattern):
    ret = 0
    for i in range(4):
        for j in range(4):
            if pattern[i][j] == '#':
                ret += 1
    return ret


def solve(cas):
    p = [[list(input()) for i in range(4)] for j in range(3)]
    if count(p[0]) + count(p[1]) + count(p[2]) != 16:
        print('No')
        return
    
    mat = [['.' for _ in range(4)] for _ in range(4)]
    
    def fill(matrix, pattern, x, y):
        m = copy(matrix)
        for i in range(x, x+len(pattern)):
            for j in range(y, y+len(pattern[0])):
                if i >= 4 or j >= 4:
                    return None
                if i-x >= len(pattern) or j-y >= len(pattern[0]):
                    return None
                if m[i][j] == '#' and pattern[i-x][j-y] == '#':
                    return None
                if m[i][j] == '.' and pattern[i-x][j-y] == '#':
                    m[i][j] = '#'
        return m
    
    for i in range(4):
        for j in range(4):
            r = rotate(p[0])
            for k in range(4):
                tmp = cut(r)
                ret = fill(mat, tmp, i, j)
                if ret is not None:
                    # printp(ret)
                    for ii in range(4):
                        for jj in range(4):
                            rr = rotate(p[1])
                            for kk in range(4):
                                ttmp = cut(rr)
                                rret = fill(ret, ttmp, ii, jj)
                                if rret is not None:
                                    for iii in range(4):
                                        for jjj in range(4):
                                            rrr = rotate(p[2])
                                            for kkk in range(4):
                                                tttmp = cut(rrr)
                                                rrret = fill(rret, tttmp, iii, jjj)
                                                if rrret is not None:
                                                        print('Yes')
                                                        return
                                                rrr = rotate(rrr)
                            rr = rotate(rr)
                r = rotate(r)
                
    print('No')

                




cas = 1
for _ in range(cas):
    solve(_)

