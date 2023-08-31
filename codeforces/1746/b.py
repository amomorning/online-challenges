import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


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

def solve(cas):
    n, = inp()
    a = inp()
    id_0, id_1 = [], []
    for i in range(n):
        if a[i]:
            id_1.append(i)
        else:
            id_0.append(i)
    if len(id_1) == 0 or len(id_0) == 0:
        print(0)
        return

    cnt = 0
    j = 0
    m = len(id_0)-1
    for i in range(len(id_1)):
        while j < m and id_0[j] < id_1[i]:
            j += 1
        if id_1[i] < id_0[j] and m >= j:
            cnt += 1
            m -= 1

    print(cnt)
        
        
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
