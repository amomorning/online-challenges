import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

n = int(input())

a = [[1] for _ in range(n)]

for i in range(1, n):
    for j in range(i-1):
        a[i].append(a[i-1][j] + a[i-1][j+1])
    a[i].append(1)
for x in a:
    printf(x)
