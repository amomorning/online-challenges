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

    cnt = 0

    flag = False
    zero = False
    for i in range(n):
        if(a[i] != 0):
            cnt += 1
        for j in range(i):
            if(a[i] == a[j]):
                flag = True
            
    if(cnt < n or flag == True):
        printf(cnt)
    else:
        printf(cnt+1)
