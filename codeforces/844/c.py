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
class Encodict:
    def __init__(self, func=lambda : 0):
        self.RANDOM = random.randint(0, 1<<32)
        self.default = func
        self.dict = {}
    
    def __getitem__(self, key):
        k = self.RANDOM ^ key
        if k not in self.dict:
            self.dict[k] = self.default()
        return self.dict[k]
    
    def __setitem__(self, key, item):
        k = self.RANDOM ^ key
        self.dict[k] = item

    def keys(self):
        return [self.RANDOM ^ i for i in self.dict]
    
    def items(self):
        return [(self.RANDOM ^ i, self.dict[i]) for i in self.dict]
    
    def sorted(self, by_value=False, reverse=False):
        if by_value:
            self.dict = dict(sorted(self.dict.items(), \
                key=lambda x:x[1], reverse=reverse))
        else:
            self.dict = dict(sorted(self.dict.items(), \
                key=lambda x:self.RANDOM^x[0], reverse=reverse))


def calc(a, b, mp):
    arr = []
    for i in range(26):
        if mp[i] != 0:
            arr.append(len(mp[i]))
        
    arr = sorted(arr)
    modify = 0
    for i in range(max(len(arr)-b, 0)):
        modify += arr[i]
        
    for x in arr:
        if x > a:
            modify += x-a
    
    modify += a * max(b-len(arr), 0)
    
    return modify


def solve(cas):
    n, = inp()
    s = input()
    mp = Encodict(collections.deque)
    for i in range(n):
        mp[ord(s[i]) - ord('a')].append(i)

    cnt = math.inf
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            # i times and n//i characters          
            if n//i <= 26:
                modify = calc(i, n//i, mp)
                if modify  < cnt:
                    cnt = modify
                    a, b = i, n//i
            # n//i times and i characters          
            if i <= 26:
                modify = calc(n//i, i, mp)
                if modify < cnt:
                    cnt = modify
                    a, b = n//i, i
                
    arr = []
    for i in range(26):
        if len(mp[i]) > 0:
            arr.append((i, mp[i]))
    
    # debug(a, b)
    arr = sorted(arr, key=lambda x: len(x[1]))
    rest = collections.deque()
    for i in range(max(len(arr)-b, 0)):
        for x in arr[i][1]:
            rest.append(x)
            arr[i] = (arr[i][0], [])
    
    # debug(arr)
    for c, li in arr:
        while len(li) > a:
            rest.append(li.pop()) 
    
    # debug(arr)
    # debug(rest)
    while len(arr) < b:
        for i in range(26):
            if len(mp[i]) == 0:
                for _ in range(a):
                    mp[i].append(rest.pop())
                arr.append((i, mp[i]))
                break
    # debug(rest)
    # debug(arr)
    
    for c, li in arr:
        if len(li) != 0:
            while len(li) < a:
                li.append(rest.pop())
    
    t = ['#']*n
    for c, li in arr:
        if len(li) != 0:
            for x in li:
                t[x] = chr(c + ord('a'))
        
    print(cnt)
    print(''.join(t))
        

    



        

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
