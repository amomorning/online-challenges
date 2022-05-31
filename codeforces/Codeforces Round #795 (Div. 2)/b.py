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
    a.append(-1)
    res = []
    for i, x in enumerate(a):
        if i == 0:
            continue
        if a[i] != a[i-1]:
            if cnt == 0:
                printf(-1)
                break
            res.append(i)
            for j in range(cnt):
                res.append(i-cnt+j)
            cnt = 0
            continue
        cnt += 1

    if(len(res) == n):
        printf(res)
    
