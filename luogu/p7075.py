#!/usr/bin/env python3
import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x() for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

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


# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout


month = [31,28,31,30,31,30,31,31,30,31,30,31]

def calc_julian(r):
    d,m,y = 1,1,-4712
    # calc year
    r += 1
    y += 4*(r//(365*4+1))
    r = r % (365*4+1)
    for i in range(4):
        if r <= 365 or (y%4==0 and r==366): 
            break
        r -= 365+(y%4==0)
        y += 1
    

    # calc month and day
    for i in range(12):
        if y%4==0 and i==1: 
            r-=29
        else: r-=month[i]
        if r<=0:
            d = r+month[i]+(y%4==0 and i==1)
            m = i+1
            break
    return d,m,y


def is_leap(y):
    return (y%4==0 and y%100!=0) or y%400==0

def calc_gregorian(r):
    d,m,y = 1,1,1583
    # calc year
    y += 400*(r//(365*400+100-3))
    r = r % (365*400+100-3)
    for i in range(400):
        if r < 365 or (is_leap(y) and r==365): 
            break
        r -= 365 + is_leap(y)
        y += 1

    if r == 0:
        return 31, 12, y-1
    
    # calc month and day
    for i in range(12):
        if is_leap(y) and i==1: 
            r-=29
        else: r-=month[i]
        if r<=0:
            d = r+month[i] + (is_leap(y) and i==1)
            m = i+1
            break
    return d, m, y


def solve(r):
    
    if r < 2299161: #before 1582.10.4
        d,m,y = calc_julian(r)
        if y <= 0:
            print(f"{d} {m} {-y+1} BC")
        else:
            print(d, m, y)
    elif r >= 2299238: #after 1583.1.1
        print(*calc_gregorian(r-2299238))
    else:
        r -= 2299161
        # r=0 -> 1582.10.5 -> 1582.10.15
        # r=16 -> 1582.10.21 -> 1582.10.31
        if r <= 16:
            print(f"{r+15} 10 1582")
            return
        else:
            r-=17
        if r <= 29:
            print(f"{r+1} 11 1582")
        else:
            r -= 30
            print(f"{r+1} 12 1582")
    




            
# l, r = 2299161, 3000000
# while l < r:
#     mid = (l+r)//2
#     d,m,y = calc_julian(mid)
#     if (y, m, d) >= (1583, 1, 1):
#         r = mid
#         ans = mid
#     else:
#         l = mid+1
# print(ans)

# for i in range(400):
# for i in range(2299160, 2299238+10):
#     print(i)
#     solve(i)

cas = 1
cas = int(input())
for _ in range(cas):
    r, = inp()
    solve(r)

