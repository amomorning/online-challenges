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

def hash_pos(s):
    s = sorted(s)
    code = [[0, 10000],[20000,30000],[40000,50000]]
    ret = 0
    for i in range(3):
        for j in range(2):
            ret += code[i][j] * s[i][j]
    return ret

        

def check(pos, n):
    if pos[0] <= 0 or pos[0] > n: return False
    if pos[1] <= 0 or pos[1] > n: return False
    return True


def bfs(start, target, n):
    target = tuple(target)
    vis = {}
    q = collections.deque()

    vis[hash_pos(start)] = True
    q.append(start)

    while q:
        u = q.popleft()

        for i in range(3):
            for j in range(3):
                if j == i: continue
                dx, dy = u[j][0] - u[i][0], u[j][1] - u[i][1]
                new_ui = (u[i][0] + 2*dx, u[i][1] + 2*dy)
                if not check(new_ui, n): continue
                # print(u[i], new_ui)
                if new_ui == target:
                    return True

                k = 3^i^j
                new_pos = [new_ui, u[j], u[k]]
                hashed_pos = hash_pos(new_pos)
                if hashed_pos not in vis:
                    vis[hashed_pos] = True
                    q.append(new_pos)

    return False



def solve(cas):
    n, = inp()    
    a = inp()
    start = []
    for i in range(3):
        start.append((a[i*2], a[i*2+1]))

    target = inp()
    # print(start)
    
    if bfs(start, target, n):
        print("YES")
    else:
        print("NO")





cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
