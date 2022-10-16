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
    h, w, sx, sy = inp()
    n, = inp()
    H = Encodict(list) 
    W = Encodict(list)
    for i in range(n):
        x, y = inp()
        H[x].append(y)
        W[y].append(x)

    for x in H.keys():
        H[x] = sorted(H[x])
    for y in W.keys():
        W[y] = sorted(W[y])
    
    q, = inp()
    for i in range(q):
        d, l = input().split()
        l = int(l)
        # debug(d)
        if d == 'L':
            idx = bisect.bisect_left(H[sx], sy) - 1
            if idx == -1 or len(H[sx]) == 0:
                sy = max(1, sy-l)
            else:
                sy = max(sy-l, H[sx][idx] + 1)
            
        if d == 'R':
            idx = bisect.bisect_left(H[sx], sy)
            if idx == len(H[sx]) or len(H[sx]) == 0:
                sy = min(w, sy+l)
            else:
                sy = min(sy+l, H[sx][idx]-1)

        if d == 'U':
            idx = bisect.bisect_left(W[sy], sx) - 1
            if idx == -1 or len(W[sy]) == 0:
                sx = max(1, sx-l)
            else:
                sx = max(sx-l, W[sy][idx] + 1)

        if d == 'D':
            idx = bisect.bisect_left(W[sy], sx) 
            if idx == len(W[sy]) or len(W[sy]) == 0:
                sx = min(h, sx+l)
            else:
                sx = min(sx+l, W[sy][idx] -1)

        print(sx, sy)



        

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
