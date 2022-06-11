import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

R, C = map(int, input().split())
a, b = map(int, input().split())
c, d = map(int, input().split())
A = [[a, b], [c, d]]
printf(A[R-1][C-1])
