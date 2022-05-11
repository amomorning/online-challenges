import sys;input=lambda:sys.stdin.readline().strip("\r\n")
import platform
LOCAL = (platform.uname().node == 'AMO')
# print(LOCAL)
def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

import bisect

for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    a.reverse()
    b = [a[0]]
    for i in range(1, n):
        b.append(b[i-1] + a[i])

    
    for i in range(q):
        x = int(input())

        r = bisect.bisect_left(b, x)
        printf(-1) if r == n else printf(r+1) 

            
