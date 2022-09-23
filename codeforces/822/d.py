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


def solve(n, k, a):
    if k == n-1: return True
    l, r = k-1, k+1
    # get current
    value, cost = 0, 0
    q = collections.deque()
    for i in range(l, -1, -1):
        value += a[i]
        cost = max(cost, -value)
        if value > 0:
            q.append((value, cost))
            value, cost = 0, 0


    tmp = a[k]
    while r < n:
        flag = False
        while q:
            u = q.popleft()
            if u[1] <= tmp:
                tmp += u[0]
                flag = True
            else:
                q.appendleft(u)
                break


        while tmp + a[r] >= 0:
            tmp += a[r]
            r += 1
            if r == n:
                return True
            flag = True
            if a[r-1] > 0:
                break
        if not flag:
            break
    return False

for _ in range(int(input())):
    n, k = inp(); k -= 1
    a = inp()
    if solve(n, k, a):
        print("YES")
        continue
    a.reverse()
    k = n-k-1
    if solve(n, k, a):
        print("YES")
    else:
        print("NO")
