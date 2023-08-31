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

c2n = lambda c: ord(c) - ord('a')
n2c = lambda x: chr(x + ord('a'))

def solve(cas):
    s = input()
    mp = Encodict(lambda:0)
    for c in s:
        mp[c2n(c)] += 1
    n = len(s)
    ans = [None] * n
    j = 0
    for i in range(26):
        if mp[i] != 0:
            for k in range(mp[i]//2):
                ans[j] = i
                ans[n-j-1] = i
                j += 1
            mp[i] %= 2
            if mp[i] != 0:
                rest = []
                for k in range(i+1, 26):
                    if mp[k] != 0:
                        rest.append(k)
                if len(rest) == 0:
                    ans[j] = i
                elif len(rest) == 1:
                    for _ in range(mp[rest[0]]//2):
                        ans[j] = rest[0]
                        ans[n-j-1] = rest[0]
                        j += 1
                    mp[rest[0]] %= 2
                    if mp[rest[0]] == 0:
                        ans[j] = i
                    else:
                        ans[j] = rest[0]
                        ans[n-j-1] = i
                else:
                    for k in range(i+1, 26):
                        while mp[k] != 0:
                            ans[j] = k
                            j += 1
                            mp[k] -= 1
                    ans[j] = i
    print(''.join(map(n2c, ans)))

            

        
    


cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)

