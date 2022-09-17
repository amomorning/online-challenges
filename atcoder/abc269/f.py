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

def odd(x):
    return int(x%2 != 0)
def even(x):
    return int(x%2 == 0)

MOD = 998244353
def norm(v):
    v = v % MOD
    if v < 0: v += MOD
    return v



n, m = inp()
q = int(input())
for i in range(q):
    a, b, c, d = map(lambda x: int(x)-1, input().split())
    
    if odd(a+c) and odd(d-c+1):
        hn = (d-c)//2
        s1 = (a*m+c+2 + a*m+d) * hn // 2 % MOD
        vn = (b-a)//2
        ans = (1+vn)*vn//2*m*2*hn%MOD + (vn+1)*s1%MOD
        if b-a > 0:
            hn = (d-c)//2+1
            s2 = ((a+1)*m+c+1 + (a+1)*m+d+1) * hn // 2 % MOD
            vn = (b-a-1)//2
            ans += (1+vn)*vn//2*m*2*hn%MOD + (vn+1)*s2%MOD
        print(ans%MOD)
    elif odd(a+c) and not odd(d-c+1):
        hn = (d-c+1)//2
        s1 = (a*m+c+2 + a*m+d+1) * hn // 2 % MOD
        vn = (b-a)//2
        ans = (1+vn)*vn//2*m*2*hn%MOD + (vn+1)*s1%MOD
        if b-a > 0:
            s2 = ((a+1)*m+c+1 + (a+1)*m+d) * hn // 2 % MOD
            vn = (b-a-1)//2
            ans += (1+vn)*vn//2*m*2*hn%MOD + (vn+1)*s2%MOD
        print(ans%MOD)
    elif not odd(a+c) and odd(d-c+1):
        hn = (d-c)//2+1
        s1 = (a*m+c+1 + a*m+d+1)*hn //2 % MOD
        vn = (b-a)//2
        ans = (1+vn)*vn//2*m*2*hn%MOD + (vn+1)*s1%MOD
        if b-a > 0:
            hn -= 1
            s2 = ((a+1)*m+c+2+ (a+1)*m+d) * hn // 2 % MOD
            vn = (b-a-1)//2
            ans += (1+vn)*vn//2*m*2*hn%MOD + (vn+1)*s2%MOD
        print(ans%MOD)
    elif not odd(a+c) and not odd(d-c+1):
        hn = (d-c+1)//2  
        s1 = (a*m+c+1 + a*m+d) * hn // 2 % MOD 
        vn = (b-a)//2
        ans = (1+vn)*vn//2*m*2*hn%MOD + (vn+1)*s1%MOD
        if b-a > 0:
            s2 = ((a+1)*m+c+2+ (a+1)*m+d+1) * hn // 2 % MOD
            vn = (b-a-1)//2
            ans += (1+vn)*vn//2*m*2*hn%MOD + (vn+1)*s2%MOD
        print(ans%MOD)
    else:
        print(-1)
        
