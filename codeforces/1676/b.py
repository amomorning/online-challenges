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


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mn = min(a)
    tot = 0
    for i in range(n):
        tot += a[i] - mn

    printf(tot)
