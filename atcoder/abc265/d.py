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

def solve():
    n, p, q, r = map(int, input().split()) 
    a = list(map(int, input().split()))
    s = [0]+ list(itertools.accumulate(a))

    # print(s)
    for x in range(n-2):
        y = bisect.bisect_left(s, s[x]+p)
        if y == n+1: break
        if s[y] - s[x] != p:
            continue
        # print(x, y)
        z = bisect.bisect_left(s, s[y]+q)
        if z == n+1: break
        if s[z] - s[y] != q:
            continue
        # print(x, y, z, s[z], s[y])
        w = bisect.bisect_left(s, s[z]+r)
        if w == n+1: break
        if s[w] - s[z] != r:
            continue
        # print(x, y, z, w)
        print("Yes")
        return
    print("No")

solve()
