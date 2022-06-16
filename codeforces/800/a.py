import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import sys; input = lambda:sys.stdin.readline().strip("\r\n")

def debug(*args):
    print('\033[92m', end='', file=sys.stderr)
    print(*args, file=sys.stderr, end='')
    print('\033[0m', file=sys.stderr)

def printf(*args):
    for arg in args:
        if isinstance(arg, typing.Iterable):
            print(' '.join(map(str, arg)), end=' ')
        else:
            print(arg, end=' ')
    print()

for _ in range(int(input())):
    a, b = map(int, input().split())

    s = ''
    if a > b:
        for i in range(a):
            s += '0'
            if b > 0:
                s += '1'
                b -= 1
    else:
        for i in range(b): 
            s += '1'
            if a > 0:
                s += '0'
                a -= 1
    print(s)
        
