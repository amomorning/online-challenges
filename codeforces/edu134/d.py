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

m = 29
for _ in range(int(input())):
    n = int(input())
    pairs = [(inp(), inp())]

    ans = 0
    for j in range(m, -1, -1):
        flag = True
        for a, b in pairs:
            cnt = [0] * 2
            for x in a:
                cnt[x>>j&1] += 1
            for x in b:
                cnt[~x>>j&1] -= 1
            flag &= (cnt[0] == 0 and cnt[1] == 0)
        if flag:
            ans += (1<<j)
            tmp = []
            for a, b in pairs:
                aa, bb = [[], []], [[], []]
                for x in a:
                    aa[x>>j&1].append(x)
                for x in b:
                    bb[x>>j&1].append(x)
                if aa[0]: tmp.append((aa[0], bb[1]))
                if aa[1]: tmp.append((aa[1], bb[0]))
            pairs = tmp

    print(ans)
