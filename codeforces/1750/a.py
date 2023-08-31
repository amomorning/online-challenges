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
    a = inp(lambda x: int(x)-1)
    p = [-1] * n
    for i in range(n):
        p[a[i]] = i
    for k in range(n-1, -1, -1):
        if a[k] != k:
            j = p[k]
            flag = False
            for i in range(j):
                if a[i] < k:
                    flag = True
                    p[a[j]], p[a[k]] = k, j
                    a[j], a[k] = a[k], a[j]
                    break
                    # debug(i, j, k)
            # debug(a)

            if not flag:
                print("No")
                return
    print("Yes")
    
        
    

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
