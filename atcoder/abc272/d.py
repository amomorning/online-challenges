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


def find_dir(m):
    dir = set()
    for i in range(math.floor(math.sqrt(m))+1):
        tmp = m - i * i
        if tmp < 0: continue
        j = math.floor(math.sqrt(tmp))
        if j*j + i*i == m:
            dir.add((i, j))
            dir.add((-i, -j))
            dir.add((-i, j))
            dir.add((i, -j))
            dir.add((j, i))
            dir.add((-j, -i))
            dir.add((-j, i))
            dir.add((j, -i))
    return list(dir)
            

def solve(cas):
    n, m = inp()    

    q = collections.deque([(0, 0)])
    vis = [[-1] * n for _ in range(n)]
    dirs = find_dir(m)
    vis[0][0] = 0
    while q:
        u = q.popleft()

        for d in dirs:
            nx, ny = (u[0] + d[0], u[1] + d[1])
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if vis[nx][ny] == -1:
                vis[nx][ny] = vis[u[0]][u[1]] + 1
                q.append((nx, ny))
    
    for i in range(n):
        printf(vis[i])
            
        
        


cas = 1
for _ in range(cas):
    solve(cas)
