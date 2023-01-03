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
class SegmentTree:
    def __init__(self, size, select=min, elem=math.inf):
        self.size = 1 << size.bit_length()
        self.tree = [elem] * (self.size << 1)
        self.select = select
        self.elem = elem
 
    def __getitem__(self, i):
        return self.tree[i + self.size]
 
    def update(self, i, x):
        i0 = i + self.size
        while i0:
            self.tree[i0] = x
            x = self.select(self.tree[i0], self.tree[i0 ^ 1])
            i0 >>= 1
 
    def query(self, i, j):
        """ query range [i, j)
        """
        x = self.elem
        l = i + self.size
        r = j + self.size
        while l < r:
            if l & 1:
                x = self.select(x, self.tree[l])
                l += 1
            if r & 1:
                x = self.select(x, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return x

def solve(cas):
    n, m = inp()
    # m -= 1
    a = inp()
    ans = 0
    # if a[m] > 0 and m > 0:
    #     a[m] = -a[m]
    #     ans += 1
    cur = 0
    st = SegmentTree(n, elem=(math.inf, -1))
    for i in range(m, n):
        st.update(i, (a[i], i))
        # debug(i, cur, cur+a[i])
        cur += a[i]
        while cur < 0:
            mn, mni = st.query(m, i+1)
            # debug(i, mn, mni, cur)
            cur += -mn * 2
            ans += 1
            a[mni] = -a[mni]
            st.update(mni, (-mn, mni))
    
    st = SegmentTree(m, max, (-math.inf, -1))
    cur = 0
    for i in range(m-1, 0, -1):
        st.update(i, (a[i], i))
        cur += a[i]
        while cur > 0:
            mx, mxi = st.query(i, m)
            cur -= 2*mx
            ans += 1
            st.update(mxi, (-mx, mxi))
            a[mxi] = -a[mxi]
    debug(a)
    debug(itertools.accumulate(a))
    print(ans)

        
cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
