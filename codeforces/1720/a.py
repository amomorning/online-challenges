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
    a, b, c, d = inp()
    ab = math.gcd(a, b)
    cd = math.gcd(c, d)
    a = a // ab
    b = b // ab
    c = c // cd
    d = d // cd

    if a * d == b * c:
        print(0)
        return
    
    if a == 0 or c == 0:
        print(1)
        return
    
    if a * d % (b * c) == 0 or b * c % (a * d) == 0:
        print(1)
        return

    print(2)


for _ in range(int(input())):
    solve()
