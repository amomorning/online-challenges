#!/usr/bin/env python3
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


# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

ans = []
def solve(cas):
    s = input()+chr(ord('a')-1)
    n = len(s)-1
    pos, = inp()

    q = [ord(s[0])]
    
    cur = n
    for i in range(1, n+1):
        oc = ord(s[i])
        if len(q) == 0 or oc >= q[-1]:
            q.append(oc)
        else:
            while q and oc < q[-1] and pos - cur > 0:
                q.pop()
                pos -= cur
                cur -= 1
            if q and oc < q[-1] and pos - cur <= 0:
                if len(q) >= pos:
                    ans.append(chr(q[pos-1]))
                    # debug(q[pos-1])
                else:
                    # debug(cur, q, pos)
                    # debug(s[i+pos-len(q)-1])
                    ans.append(s[i+pos-len(q)-1])
                return
            q.append(oc)
                


cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)


print(''.join(ans))
