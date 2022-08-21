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

n, m = inp()
mx = [int('1'*31, 2)] * n
e = [[] for _ in range(n)]
for i in range(m):
    i, j, x = inp(); i-=1; j-=1
    if i > j: i, j = j, i
    mx[i] &= x; mx[j] &= x
    e[i].append((j, x))
# print(mx)
a = [0] * n
for u in range(n):
    if len(e[u]) == 0: continue
    
    for v, x in e[u]:
        a[u] |= mx[v] ^ x
        a[v] |= mx[u] ^ x

for u in range(n):
    for v, x in e[u]:
        a[v] |= x ^ (a[u] | a[v])

print(' '.join(map(str, a)))

