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

from bisect import bisect_right


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    m = int(input())
    b = list(map(int, input().split()))
    b = sorted(b)

    win = False
    for i in range(n):
        cur = a[i]
        status = 1
        while True:
            if status == 1:
                idx = bisect_right(b, cur)
                if idx >= m: 
                    win = True
                    break
                cur = b[idx]
            else:
                idx = bisect_right(a, cur)
                if idx >= n:
                    break
                cur = a[idx]

            status ^= 1
    printf("Alice") if win else printf("Bob")
                
            

    win = False
    for i in range(m):
        cur = b[i]
        status = 0
        while True:
            if status == 1:
                idx = bisect_right(b, cur)
                if idx >= m: 
                    break
                cur = b[idx]
            else:
                idx = bisect_right(a, cur)
                if idx >= n:
                    win = True
                    break
                cur = a[idx]

            status ^= 1
    printf("Bob") if win else printf("Alice")
