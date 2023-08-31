import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(float, input().split()))

    b = []
    for i in range(n-1):
        if a[i] < a[i+1] * 2:
            b.append(1)
        else:
            b.append(0)
        
    b = ''.join(map(str, b))

    cnt = 0
    for s in b.split('0'):
        if len(s) >= k:
            cnt += len(s)-k+1

    printf(cnt)
