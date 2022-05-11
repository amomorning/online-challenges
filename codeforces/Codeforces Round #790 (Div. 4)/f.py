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
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    a.append(-1)

    l = []
    cnt = 1
    for i in range(1, n+1):
        if(a[i] != a[i-1]):
            if(cnt >= k):
                l.append(a[i-1])
            cnt = 0
        cnt += 1

    # printf(l)

    if(len(l) == 0):
        print(-1)
        continue
    
    l = sorted(l)
    left = 0
    
    mxl = 0
    for i in range(len(l)):
        if i == 0:
            mxl = 1
        else:
            if l[i] - l[i-1] != 1:
                if(i-left > mxl):
                    mxl = i-left
                    res = (l[left], l[i-1])
                left = i
    
    if len(l) - left >= mxl:
        res = (l[left], l[-1])
    print(res[0], res[1])
    
    


            
