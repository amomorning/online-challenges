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
    a = list(map(int, input().split()))
    tot = 0
    for i in range(1, 4):
        if a[i] > a[0]:
            tot += 1
    printf(tot)
