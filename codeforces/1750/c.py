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

def solve(cas):
    n, = inp()
    s = list(map(int, input()))
    t = list(map(int, input()))
    xors = list(set([s[i]^t[i] for i in range(n)]))
    if len(xors) > 1:
        print("NO")
        return

    ans = []
    if xors[0] == 0:
        for i in range(n):
            s[i] = 1-s[i]
        ans.append((0, n-1))
        # print(1, n)
    
    ss = list(set(s))
    if len(ss) == 1 and ss[0] == 0:
        ans.append((0, 0))
        ans.append((1, n-1))
        ans.append((0, n-1))
    elif len(ss) == 1 and ss[0] == 1:
        ans.append((0, n-1))
    else:
        op, l = 0, 0
        while l < n:
            # debug(s[l])
            if s[l] == 1:
                r = l
                while r < n and s[r] == 1:
                    r += 1
                ans.append((l, r-1))
                l = r
                op += 1
            else:
                l += 1

        if op%2 == 0:
            ans.append((0, 0))
            ans.append((1, n-1))
            ans.append((0, n-1))
    

    print('YES')
    print(len(ans))
    for l, r in ans:
        print(l+1, r+1)
        

    # for i in range(n):

        

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
