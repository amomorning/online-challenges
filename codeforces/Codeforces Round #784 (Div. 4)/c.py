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

    # printf(a)

    cnt = 0
    for i in range(0, n, 2):
        cnt += (a[i] % 2)
    flag = (cnt == 0) or (cnt == n - (n // 2))

    cnt = 0
    for i in range(1, n, 2):
        cnt += (a[i] % 2)
    flag &= (cnt == 0) or (cnt == n // 2)

    printf("YES") if flag else printf("NO")
    