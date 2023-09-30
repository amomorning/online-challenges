
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

def add(a, b, c):
    ret = make_arr(4, 4)(lambda:0)
    for i in range(4):
        for j in range(4):
            ret[i][j] = a[i][j] | b[i][j] | c[i][j]
    return sum([sum(x) for x in ret])
            

def solve(cas):
    p = [[list(input()) for i in range(4)] for j in range(3)]
    tot = 0
    for k in range(3):
        for i in range(4):
            for j in range(4):
                if p[k][i][j] == '#': tot += 1
    if tot != 16:
        print('No')
        return

    def fill(pattern, x, y):
        mat = make_arr(4, 4)(lambda:0)
        for i in range(x, x+len(pattern)):
            for j in range(y, y+len(pattern[0])):
                if i >= 4 or j >= 4: return None
                if pattern[i-x][j-y] == '#':
                    mat[i][j] = 1
        return mat


    P = [[], [], []]
    for k in range(3):
        r = p[k]
        for _ in range(4):
            for i in range(4):
                for j in range(4):
                    ret = fill(cut(r), i, j)
                    if ret != None:
                        P[k].append(ret)
            r = rotate(r)
    for a in P[0]:
        for b in P[1]:
            for c in P[2]:
                if add(a, b, c) == 16:
                    print('Yes')
                    return
    print('No')
            

cas = 1
for _ in range(cas):
    solve(_)

