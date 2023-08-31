import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

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
    n, q = inp()
    a = inp()
    s, sa = [0] * (n+1), [0] * (n+1)
    for i in range(n-1, -1, -1):
        s[i] = a[i] ^ s[i+1]
        sa[i] = a[i] + sa[i+1]

    # debug(s)
    # debug(sa)
    mp = Encodict(list)
    pm = Encodict(list)
    for i in range(n):
        mp[s[i]].append(i)
        if len(pm[s[i]]) == 0:
            pm[s[i]].append(i%2)
        else:
            pm[s[i]].append(pm[s[i]][-1] + (i%2))
    


    for i in range(q):
        l, r = inp(lambda x: int(x)-1)
        if sa[l] - sa[r+1] == 0:
            print(0)
            continue
        if s[l] ^ s[r+1] == 0:
            if (r-l+1)%2 != 0:
                print(1)
                continue
            if a[r] == 0 or a[l] == 0:
                print(1)
                continue
        if s[l] == s[r+1]:
            L, R = bisect.bisect_left(mp[s[l]], l), bisect.bisect_left(mp[s[l]], r+1)
            # debug(l, r)
            # debug(mp[s[l]])
            # debug(pm[s[l]])
            # debug(L, R)

            if l % 2 == 0 and pm[s[l]][R-1] - pm[s[l]][L] != 0 and R-L-1 >= 1:
                print(2)
                continue
            if l % 2 == 1 and pm[s[l]][R-1] - pm[s[l]][L] != R-L-1 and R-L-1 >= 1:
                print(2)
                continue

        print(-1)
        


def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
