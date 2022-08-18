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

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, list(input()))))

    flag = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                flag = max(flag, 1)
            
            if j < m-1 and i < n-1 and a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1] <= 2:
                flag = max(flag, 2)
            
    
    # print('flag: ', flag)
    
    tot = sum([sum(a[i]) for i in range(n)])
    if flag == 0:
        print(tot-2)
    elif flag == 1:
        print(tot-1)
    else:
        print(tot)
                
