import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

from itertools import accumulate

for _ in range(int(input())):
    n, k = map(int, input().split())
    
    a = list(accumulate(map(int, input().split())))
    if k >= n:
        printf(a[-1] + n * k - (n + 1) * n // 2)
    else:
        mx = a[k-1]
        for i in range(k, n):
            mx = max(mx, a[i] - a[i-k])
        printf(mx + k * (k - 1) // 2)
