import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))
sys.setrecursionlimit(10**6)

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


def solve(cas):
    s = input()
    if len(s) != 8:
        print("No")
        return
    if s[0] <= 'Z' and s[0] >= 'A' and s[-1] <= 'Z' and s[-1] >= 'A':
        digits = s[1:-1]
        try:
            if str(int(digits)) == digits:
                print("Yes")
                return
        except ValueError:
            pass
    print("No")
    return


cas = 1
for _ in range(cas):
    solve(cas)

