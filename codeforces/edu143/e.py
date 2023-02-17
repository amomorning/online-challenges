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

# avaliable on Google, AtCoder
# sys.setrecursionlimit(10**6)
# import numpy as np
# import scipy

# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

class Stack(list):
    def __init__(self, iterable=None):
        if iterable is not None:
            super().__init__(item for item in iterable)
    
    def push(self, *args):
        if len(args) == 1:
            self.append(args[0])
        else:
            self.append(args)
    
    def back(self):
        return self[-1]
    
    def empty(self):
        return len(self) == 0
    
    def length(self):
        return len(self)
    
class Boom:
    def __init__(self) -> None:
        self.stack = Stack()
        self.sum = 0
    
    def append(self, h):
        l1, h1 = 1, h
        while self.stack and self.stack.back()[1] > h1-l1:
            l0, h0 = self.stack.pop()
            self.sum -= (h0 + h0 - l0 + 1) * l0 // 2
            l1 += l0
        l1 = min(l1, h1)
        self.sum += (h1 + h1 - l1 + 1) * l1 // 2
        self.stack.push(l1, h1)


def solve(cas):
    n, = inp()
    h = inp()
    f = [0] * n
    boom = Boom()
    for i in range(n):
        boom.append(h[i])
        f[i] += boom.sum - h[i]
    
    boom = Boom()
    for i in range(n-1, -1, -1):
        boom.append(h[i])
        f[i] += boom.sum - h[i] 
    
    res = sum(h) - max(f)
    print(res)
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

