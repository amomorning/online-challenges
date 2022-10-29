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
    if n == 0:
        print(1)
        return

    vis = {}
    a = [n]
    cur = 0
    vis[0] = 1
    while cur < len(a):
        l, r = a[cur]//2, a[cur]//3
        cur += 1
        if not l in vis:
            vis[l] = 1
            a.append(l)
        if not r in vis:
            vis[r] = 1
            a.append(r)
    a = sorted(a)
    # debug(a)
    f = {}
    f[0] = 1
    for x in a:
        f[x] = f[x//2] + f[x//3]
    print(f[n])
        

        

        
    

    
        

cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
