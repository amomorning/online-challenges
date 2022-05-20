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
    x = list(map(int, input().split()))
    a = []
    for i in range(3):
        a.append((x[i], i))
    a = sorted(a)

    x, y, z = a[0][0]+a[1][0]+a[2][0], a[1][0]+a[2][0], a[2][0]

    b = []
    b.insert(a[0][1], x)
    b.insert(a[1][1], y)
    b.insert(a[2][1], z)
    printf(b)



