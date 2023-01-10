import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

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

# avaliable on Google, AtCoder
# sys.setrecursionlimit(10**6)
# import numpy as np
# import scipy

# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

def solve(cas):
    s = input()
    if s[0] == 'a':
        left, right = -1, -1        
        for i in range(1, len(s)):
            if s[i] == 'b' and left == -1:
                left = i
            if s[i] == 'a':
                right = i
        if left != -1 and right > left:
            print(s[:left], s[left:right], s[right:])
            return
        if left == len(s)-1:
            print(s[0:-2], s[-2], s[-1])
            return
        if left != -1:
            print(s[0:left], s[left:-1], s[-1])
            return
        if right != -1:
            print(s[0], s[1:-1], s[-1])
            return
            
    if s[0] == 'b':
        left, right = -1, -1        
        for i in range(1, len(s)):
            if s[i] == 'a' and left == -1:
                left = i
            if s[i] == 'b':
                right = i
        if left != -1 and right > left:
            print(s[:left], s[left:right], s[right:])
            return
        if left == len(s)-1:
            print(s[0], s[1:-1], s[-1])
            return
        if left != -1:
            print(s[0:left], s[left], s[left+1:])
            return
        if right != -1:
            print(s[0], s[1:-1], s[-1])        
            return
    print(":(")
    


cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
