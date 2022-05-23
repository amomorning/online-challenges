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
    a = list(map(int, list(input())))

    tot = sum(a)
    if tot % 2 == 1 or tot == 0:
        printf("NO")
        continue


    printf("YES")

    root = n-1
    while a[root-1] == 0:
        root -= 1

    u = root
    
    for i in range(1, n):
        v = (i + root) % n
        printf([u + 1, v + 1])

        u = v if a[v] == 0 else root


        
