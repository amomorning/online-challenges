import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

from bisect import bisect_left
from itertools import accumulate

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    a = sorted(a)
    s = list(accumulate(a))

    for _ in range(q):
        o = int(input())
        idx = bisect_left(a, o)
        if idx == 0:
            ans = s[n-1] - o*n
        elif idx == n:
            ans = o*n - s[n-1]
        else:
            ans = o*idx - s[idx-1] + (s[n-1]-s[idx-1]) - o*(n-idx)

            
        # ans = o*idx - s[idx] + s[n-1] - s[idx] + a[idx] - o*(n-idx)
        printf(ans)

solve()
