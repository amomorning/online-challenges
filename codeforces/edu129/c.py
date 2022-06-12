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
    b = list(map(int, input().split()))

    result = []
    for i in range(1, n):
        if a[i] < a[i-1]:

            idx = 0
            for j in range(i):
                if a[j] <= a[i]:
                    idx = j+1
            tmp = a[i]
            del a[i]
            a.insert(idx, tmp)

            tmp = b[i]
            del b[i]
            b.insert(idx, tmp)

            for j in range(i-1, idx-1, -1):
                result.append([j+1, j+2])
    
    flag = True
    for i in range(1, n):
        if b[i] < b[i-1]:
            idx = 0 
            for j in range(i):
                if b[j] <= b[i]:
                    idx = j+1
            
            for j in range(idx, i+1):
                if a[j] != a[idx]:
                    flag = False

            if(flag):
                tmp = b[i]
                del b[i]
                b.insert(idx, tmp)
                for j in range(i-1, idx-1, -1):
                    result.append([j+1, j+2])


    if flag == True:
        printf(len(result))
        for r in result:
            printf(r)
    else:
        printf(-1)
