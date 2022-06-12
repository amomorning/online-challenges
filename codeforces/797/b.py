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
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    diff = []
    for i in range(n):
        if b[i] != 0:
            diff.append(a[i] - b[i])
    
    
    flag = True
    dn = len(diff)
    for i in range(dn):
        if diff[i] < 0:
            flag = False
            break
    for i in range(1, dn):
        if diff[i] != diff[i-1]:
            flag = False
            break
    
    if dn > 0 and flag:
        for i in range(n):
            a[i] -= min(a[i], diff[0])
            if a[i] != b[i]:
                flag = False
                break

    printf("YES") if flag else printf("NO")


