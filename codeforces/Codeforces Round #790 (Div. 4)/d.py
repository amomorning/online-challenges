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
    n, m = map(int, input().split())

    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    # print(a)
    mx = max(m, n)
    
    res = 0
    for i in range(n):
        for j in range(m):

            tot = a[i][j]
            for k in range(1, mx):
                if i-k >= 0 and j-k >= 0:
                    tot += a[i-k][j-k]
                if i-k >= 0 and j+k < m:
                    tot += a[i-k][j+k]
                if i+k < n and j-k >= 0:
                    tot += a[i+k][j-k]
                if i+k < n and j+k < m:
                    tot += a[i+k][j+k]
            res = max(res, tot)
    
    printf(res)
                

    
