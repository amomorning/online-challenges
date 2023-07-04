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



class BinaryTrie:
    MAXBIT = 30
    class Node:
        def __init__(self, v):
            self.l = None
            self.r = None
            self.v = v
            self.cnt = 0
            self.xor = 1<<BinaryTrie.MAXBIT
    
    def __init__(self):
        self.root = self.Node(1<<self.MAXBIT)
    
    def insert(self, v):
        u = self.root
        stack = []
        for b in range(self.MAXBIT)[::-1]:
            stack.append(u)
            if v & (1<<b):
                if u.r is None:
                    u.r = self.Node(v)
                u = u.r
            else:
                if u.l is None:
                    u.l = self.Node(v)
                u = u.l
        u.cnt = 1
        u.v = v
        u.xor = 1<<self.MAXBIT
    
        for u in stack[::-1]:
            u.cnt = 0
            if u.l and u.l.cnt:
                u.cnt += u.l.cnt
                u.xor = min(u.xor, u.l.xor)
                u.v = u.l.v
            if u.r and u.r.cnt:
                u.cnt += u.r.cnt
                u.xor = min(u.xor, u.r.xor)
                u.v = u.r.v
            if u.l and u.r and u.l.cnt and u.r.cnt:
                u.xor = min(u.xor, u.l.v ^ u.r.v)

    def erase(self, v):
        u = self.root
        stack = []
        for b in range(self.MAXBIT)[::-1]:
            stack.append(u)
            if v & (1<<b):
                u = u.r
            else:
                u = u.l
        u.cnt = 0
        u.v = -1
        u.xor = 1<<self.MAXBIT

        for u in stack[::-1]:
            u.cnt = 0
            u.xor = 1<<self.MAXBIT
            if u.l and u.l.cnt:
                u.cnt += u.l.cnt
                u.xor = min(u.xor, u.l.xor)
                u.v = u.l.v
            if u.r and u.r.cnt:
                u.cnt += u.r.cnt
                u.xor = min(u.xor, u.r.xor)
                u.v = u.r.v
            if u.l and u.r and u.l.cnt and u.r.cnt:
                u.xor = min(u.xor, u.l.v ^ u.r.v)
            if u.cnt == 0:
                u.v = -1

def solve():
    trie = BinaryTrie()
    dic = {}
    same = 0
    for _ in range(int(input())):
        t, *q = inp()
        if t == 1:
            x = q[0]
            if x not in dic:
                dic[x] = 0
            dic[x] += 1
            if dic[x] == 1:
                trie.insert(x)
            elif dic[x] == 2:
                same += 1
        elif t == 2:
            x = q[0]
            dic[x] -= 1
            if dic[x] == 0:
                trie.erase(x)
            elif dic[x] == 1:
                same -= 1
        else:
            if same:
                print(0)
            else:
                print(trie.root.xor)


solve()
