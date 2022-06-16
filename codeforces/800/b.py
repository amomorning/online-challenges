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
    
def calc(x):
    return x * (x - 1) // 2

for _ in range(int(input())):
    n = int(input())
    s = input()

    tot = calc(n) + n 

    segs = []

    cnt = 1
    cur = s[0]
    for i in range(1, n):
        if s[i] != cur:
            segs.append(cnt)

            cur = s[i]  
            cnt = 0

        cnt += 1 
    segs.append(cnt)


    now = 0 
    m = len(segs)
    for i, x in enumerate(segs):
        now += x
        if i != m-1:
            tot -= x * (n - now - (m-i-1))
        tot -= calc(x)
            
    # printf(segs)
    print(tot)
