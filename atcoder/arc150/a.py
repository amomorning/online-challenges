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

def count_prefix(s, x, n):
    pre = [0]
    for i in range(n):
        tmp = 1 if s[i] == x else 0
        pre.append(pre[-1] + tmp)
    return pre


def solve(cas):
    n, k = inp() 
    s = input()
    
    prev_zero = count_prefix(s, '0', n)
    prev_one = count_prefix(s, '1', n)
    debug(prev_zero)
    debug(prev_one)

    cnt = 0
    for i in range(n-k+1):
        if prev_one[i] > 0: break
        if prev_zero[i+k] == prev_zero[i] and prev_one[i+k] == prev_one[-1]:
            debug(i, i+k)
            cnt += 1
        
    if cnt == 1:
        print("Yes")
    else:
        print("No")


cas = 1
cas = int(input())
for _ in range(cas):
    solve(cas)
