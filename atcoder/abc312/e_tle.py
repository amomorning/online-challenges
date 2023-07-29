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

def sixface(x, y, z, a, b, c, i):
    ret = [
        (x, y, z, a, b, z, i),
        (x, y, z, a, y, c, i),
        (x, y, z, x, b, c, i),
        (x, y, c, a, b, c, i),
        (x, b, z, a, b, c, i),
        (a, y, z, a, b, c, i)
    ]
    return ret

def solve(cas):
    n, = inp()
    x = Encodict(list)
    y = Encodict(list)
    z = Encodict(list)
    all_cubes = []
    d = {}
    
    for i in range(n):
        coords = inp()
        all_cubes.append(coords)
        for f in sixface(*coords, i):
            if f[0] == f[3]:
                x[f[0]].append(f)
            if f[1] == f[4]:
                y[f[1]].append(f)
            if f[2] == f[5]:
                z[f[2]].append(f)
    
    def check(x0, y0, a0, b0, x1, y1, a1, b1):
        if x1 >= x0 and y1 >= y0 and x1 < a0 and y1 < b0:
            return True
        if a1 > x0 and b1 > y0 and a1 <= a0 and b1 <= b0:
            return True
        if x0 >= x1 and y0 >= y1 and x0 < a1 and y0 < b1:
            return True        
        if a0 > x1 and b0 > y1 and a0 <= a1 and b0 <= b1:
            return True
        return False
    
        
    for xx in x.keys():
        for i in range(1, len(x[xx])):
            for j in range(i):
                if check(x[xx][i][1], x[xx][i][2], x[xx][i][4],x[xx][i][5],x[xx][j][1], x[xx][j][2], x[xx][j][4],x[xx][j][5]):
                    debug(x[xx][i], x[xx][j])
                    d[x[xx][i]] = d.get(x[xx][i], 0) + 1
                    d[x[xx][j]] = d.get(x[xx][j], 0) + 1
    for yy in y.keys():
        for i in range(1, len(y[yy])):
            for j in range(i):
                if check(y[yy][i][0], y[yy][i][2], y[yy][i][3],y[yy][i][5],y[yy][j][0], y[yy][j][2], y[yy][j][3],y[yy][j][5]):
                    debug(y[yy][i], y[yy][j])
                    d[y[yy][i]] = d.get(y[yy][i], 0) + 1
                    d[y[yy][j]] = d.get(y[yy][j], 0) + 1

    for zz in z.keys():
        for i in range(1, len(z[zz])):
            for j in range(i):
                if check(z[zz][i][0], z[zz][i][1], z[zz][i][3],z[zz][i][4],z[zz][j][0], z[zz][j][1], z[zz][j][3],z[zz][j][4]):
                    debug(z[zz][i], z[zz][j])
                    d[z[zz][i]] = d.get(z[zz][i], 0) + 1
                    d[z[zz][j]] = d.get(z[zz][j], 0) + 1
    debug(d)
    for i, coords in enumerate(all_cubes):
        faces = sixface(*coords, i)
        tot = 0
        for f in faces:
            tot += d.get(f, 0)
        print(tot)

cas = 1
for _ in range(cas):
    solve(_)

