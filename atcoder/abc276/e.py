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

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs(mp, s, n, m):
    vis = [[[0, 0, 0, 0] for _ in range(m)] for _ in range(n)]
    for i in range(4):
        sx, sy = s[0] + dir[i][0], s[1] + dir[i][1]
        q = collections.deque()
        if sx >= 0 and sx < n and sy >= 0 and sy < m and mp[sx][sy] == '.':
            q.append((sx, sy))
        while q:
            ux, uy = q.popleft()
            for dx, dy in dir:
                nx, ny = ux + dx, uy + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and mp[nx][ny] == '.' and vis[nx][ny][i] == 0:
                    vis[nx][ny][i] = 1
                    q.append((nx, ny))
        
    for i in range(n):
        for j in range(m):
            if i == s[0] and j == s[1]: continue
            if sum(vis[i][j]) > 1:
                print("Yes")
                return
    print("No")
    return

def solve(cas):
    n, m = inp()
    mp = [input() for _ in range(n)] 
    for i in range(n):
        for j in range(m):
            if mp[i][j] == 'S':
                bfs(mp, (i, j), n, m)
                return


def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

cas = 1
for _ in range(cas):
    solve(cas)
