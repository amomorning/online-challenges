import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda : list(map(int, input().split()))

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

MAXN = 201
for _ in range(int(input())):
    n = int(input())
    a = inp()
    mp = Encodict(list)
    for i, x in enumerate(a):
        mp[x].append(i)

    edges = []
    for ai in mp.keys():
        for aj in mp.keys():
            for p in range(len(mp[ai])-1, -1, -1):
                q = len(mp[aj]) - 1
                i = mp[ai][p]
                if mp[aj][q] < mp[ai][p]: continue
                while q > 0 and mp[aj][q-1] > i: 
                    q -= 1
                for qq in range(q, len(mp[aj])):
                    j = mp[aj][qq]
                    if ai ^ j < aj ^ i:
                        edges.append((i, j))

    # print(edges)
    edges = sorted(edges, key=lambda x: x[1])
    # print(edges)
    edges.reverse()
    dp = [1] * MAXN
    for u, v in edges:
        dp[u] = max(dp[u], dp[v]+1)
    
    
    print(max(dp))

    

    
