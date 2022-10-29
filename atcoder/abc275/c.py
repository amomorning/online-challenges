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

def valid(s, i, j):
    if i < 0 or i >= 9: return False
    if j < 0 or j >= 9: return False
    if s[i][j] == '.': return False
    return True

def solve(cas):
    s = [input() for _ in range(9)]
    
    cnt = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '.': continue
            for ii in range(i, 9):
                for jj in range(j+1, 9):
                    if not valid(s, ii, jj): continue
                    # debug((i, j), (ii, jj))
                    # debug('----------')
                    # debug(i+(jj-j), j-(ii-i))
                    if not valid(s, i+(jj-j), j-(ii-i)): continue
                    # debug(ii+(jj-j), jj-(ii-i))
                    if not valid(s, ii+(jj-j), jj-(ii-i)): continue

                    cnt += 1
    print(cnt)
                


cas = 1
# cas = int(input())
for _ in range(cas):
    solve(cas)
