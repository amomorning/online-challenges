import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')

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


def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

def solve(cas):
    n, m = inp()    
    a = inp()
    f = make_arr(m+1, 2)(math.inf)
    f[0][0] = 0
    for i in range(n):
        g = make_arr(m+1, 2)(math.inf)
        for j in range(m+1):
            for k in range(2):
                if f[j][k] != math.inf:
                    g[j][1] = min(g[j][1], f[j][k] + int(k==0))
                    if j + a[i] <= m:
                        g[j+a[i]][0] = min(g[j+a[i]][0], f[j][k])
        f = g
    # debug(dp)
    for i in range(1, m+1):
        ans = min(f[i][0], f[i][1])
        print(-1) if ans == math.inf else print(ans)

cas = 1
for _ in range(cas):
    solve(cas)
