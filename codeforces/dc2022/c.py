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
    start = []
    for i in range(3):
        start.append((a[i*2], a[i*2+1]))
    target = inp()

    for i in range(3):
        for j in range(3):
            if j == i: continue

            if target[0] == start[i][0] and target[0] == start[j][0]:
                print('YES')
                return
            if target[1] == start[i][1] and target[1] == start[j][1]:
                print('YES')
                return
            
    if sorted(start) == sorted([(1, 1), (1, 2), (2, 1)]):
        print('NO')
        return
    if sorted(start) == sorted([(n, 1), (n, 2), (n-1, 1)]):
        print('NO')
        return
    if sorted(start) == sorted([(1, n), (1, n-1), (2, n)]):
        print('NO')
        return
    if sorted(start) == sorted([(n, n), (n-1, n), (n, n-1)]):
        print('NO')
        return
    
    for x, y in start:
        dx = abs(target[0] - x)
        dy = abs(target[1] - y)
        if dx % 2 == 0 and dy % 2 == 0:
            print('YES')
            return
    print('NO')

        
    

cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
