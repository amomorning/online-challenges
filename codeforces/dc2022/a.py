import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


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

def solve(cas):
    n, k = inp()
    s = input()
    mp = Encodict(lambda : 0)
    for i in range(n):
        mp[ord(s[i]) - ord('a')] += 1
    # print(mp.items())
    m = n // k
    mex = []
    for i in range(k):
        cnt = 0
        cur = -1
        for j in range(26):
            if mp[j] <= 0 and cur == -1:
                cur = j
            if mp[j] > 0:
                mp[j] -= 1
                cnt += 1
            if cnt * k == n:
                if cur == -1:
                    cur = j+1
                break
        mex.append(cur)
    
    print(''.join(map(lambda x: chr(x+ord('a')), mex)))
        

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
